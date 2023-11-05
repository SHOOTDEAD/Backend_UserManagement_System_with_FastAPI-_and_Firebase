import firebase_admin
from firebase_admin import auth, firestore
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import requests
import json
import re
from paths import firebasesdk_file_path,API_KEY,DatabaseUrl

cred_obj = firebase_admin.credentials.Certificate(
    firebasesdk_file_path
)

app = firebase_admin.initialize_app(
    cred_obj,
    {
        "databaseURL": DatabaseUrl
    },
)

ref = firestore.client().collection("Users")


def createUser(email, password, full_name, username):
    """
    Creates a new user in firebase and stores user related information in firestore

    :param email : emailid of the user
    :param password : password for the user
    :param full_name : name of the user
    :param username : username of the user

    :returns : JSONResponse with success message or HTTPException with error message
    """

    if not validate_password(password):
        return HTTPException(
            status_code=400,
            detail="Weak password provided. Password must be at least 8 characters long and contain a mix of upper and lower case letters and digits.",
        )
    if not check_duplicate_username(username):
        return HTTPException(status_code=403, detail="Username already exists")
    try:
        user = auth.create_user(email=email, password=password)

    except firebase_admin.auth.EmailAlreadyExistsError:
        return HTTPException(status_code=403, detail="Email already exists")

    except Exception as e:
        return HTTPException(status_code=520, detail="Something went wrong")
    user_data_ref = ref.document(user.uid)
    user_data_ref.set(
        {
            "username": username,
            "email": email,
            "full_name": full_name,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
    return JSONResponse({"message": "User created successfully"}, status_code=200)


def login(email, password):
    """
    Logs in a user with credentials

    :param email : emailid of the user
    :param password : password of the user

    :returns : JSONResponse with success message or HTTPException with error message



    """

    request_ref = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={0}".format(
        API_KEY
    )
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
    request_object = requests.post(request_ref, headers=headers, data=data)
    if request_object.json().get("error"):
        return HTTPException(status_code=401, detail="Invalid login credentials")

    return JSONResponse(
        {"Firebase Auth token": request_object.json()["idToken"]}, status_code=200
    )


def auth_token(token):
    """
    Authenticates user based on authentication token

    :param token : user auth token

    :returns : user id

    """
    return auth.verify_id_token(token)["uid"]


def get_user_data(idToken):
    """
    Gets user data from firestore

    :params idToken : user auth token

    :returns : JSONReponse with user data

    """
    userid = auth_token(idToken)
    data = ref.document(userid).get().to_dict()

    return JSONResponse(data, status_code=200)


def update_user_info(idToken, user_update_info):
    """
    Update user information

    :param idToken : user auth token
    :param user_update_info : users updated information

    :returns : JSONResponse with success message or HTTPException with error message

    """
    userid = auth_token(idToken)
    if user_update_info.get("username"):
        if not check_duplicate_username(user_update_info["username"]):
            return HTTPException(status_code=403, detail="Username already exists")
    try:
        if "email" in user_update_info.keys():
            auth.update_user(userid, email=user_update_info["email"])
    except firebase_admin.auth.EmailAlreadyExistsError:
        return HTTPException(status_code=403, detail="Email already exists")

    user_update_info = {k: v for k, v in user_update_info.items() if v}
    ref.document(userid).update(user_update_info)
    return JSONResponse({"message": "User Info updated successfully"}, status_code=200)


def delete_user(idToken):
    """
    Deletes user and user information from firestore

    :param idToken : user auth token

    :returns : JSONResponse with success message

    """
    userid = auth_token(idToken)
    auth.delete_user(userid)
    user = ref.document(userid)
    user.delete()
    return JSONResponse({"message": "User Deleted"}, status_code=200)


def validate_password(password):
    """
    Validates the strength of the users password

    :param password : users password

    :return : True or False

    """
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$"
    if re.match(pattern, password):
        return True
    return False


def check_duplicate_username(username):
    """
    Validates the uniqueness of username

    :param username : username of the user

    :return : True or False

    """
    for i in ref.stream():
        if username == i.to_dict()["username"]:
            return False
    return True


def Reset_password(idToken, password):
    """
    Resets user password

    :param idToken : user auth token

    :returns : JSONResponse with success message or HTTPException with error message

    """
    if not validate_password(password):
        return HTTPException(
            status_code=400,
            detail="Weak password provided. Password must be at least 8 characters long and contain a mix of upper and lower case letters and digits.",
        )
    userid = auth_token(idToken)
    auth.update_user(userid, password=password)
    return JSONResponse({"message": "password changed successfully"}, status_code=200)
