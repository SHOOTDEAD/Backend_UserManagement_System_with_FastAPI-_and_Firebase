from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from schema import user, credentials, user_update, reset_password
import json
from firebase import (
    createUser,
    login,
    get_user_data,
    update_user_info,
    delete_user,
    Reset_password,
)
from middleware import rate_limit
from paths import firebasesdk_file_path,API_KEY,DatabaseUrl
app = FastAPI()

use_limit = 100  # no of request permitted
usage_time = 60  # time in seconds


# Endpoint for user creation
@app.post("/Create_user")
@rate_limit(use_limit, usage_time)
async def User_Registration(request: Request, userData: user):
    response = createUser(
        userData.email, userData.password, userData.full_name, userData.username
    )

    return response


# Endpoint for user login
@app.post("/Login")
@rate_limit(use_limit, usage_time)
async def User_Login(request: Request, credentials: credentials):
    response = login(credentials.email, credentials.password)

    return response


# Endpoint for user information retrival
@app.get("/User_info")
@rate_limit(use_limit, usage_time)
async def User_Info(request: Request, userdata: dict = Depends(login)):
    if type(userdata) != JSONResponse:
        return userdata
    userdata = userdata.body.decode("utf-8")
    userid = json.loads(userdata).get("Firebase Auth token")
    response = get_user_data(userid)

    return response


# Endpoint to update user information
@app.put("/User_info")
@rate_limit(use_limit, usage_time)
async def User_Info(
    request: Request, user_updated_info: user_update, userdata: dict = Depends(login)
):
    if type(userdata) != JSONResponse:
        return userdata

    userdata = userdata.body.decode("utf-8")

    userid = json.loads(userdata).get("Firebase Auth token")
    response = update_user_info(userid, user_updated_info.model_dump())

    return response


# Endpoint to delete user and user information
@app.delete("/Delete_User")
@rate_limit(use_limit, usage_time)
async def Delete_User(request: Request, userdata=Depends(login)):
    if type(userdata) != JSONResponse:
        return userdata

    userdata = userdata.body.decode("utf-8")
    userid = json.loads(userdata).get("Firebase Auth token")
    response = delete_user(userid)

    return response


@app.put("/Reset_password")
@rate_limit(use_limit, usage_time)
async def Reset_Password(
    request: Request, new_password: reset_password, userdata=Depends(login)
):
    if type(userdata) != JSONResponse:
        return userdata

    userdata = userdata.body.decode("utf-8")
    userid = json.loads(userdata).get("Firebase Auth token")
    response = Reset_password(userid, new_password.new_password)

    return response
