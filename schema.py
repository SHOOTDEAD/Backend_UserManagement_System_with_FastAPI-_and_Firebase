from pydantic import BaseModel, EmailStr
from typing import Optional


class user(BaseModel):
    """
    This pydantic model represents the input data needed to create user

    Attributes:
        email : emailid of the user
        password : password of the user
        full_name : full_name of the user
        username : username of the user

    """

    email: EmailStr
    password: str
    full_name: str
    username: str


class credentials(BaseModel):
    """
    This pydantic model represents the input data needed to login

    Attributes:
        email : emailid of the user
        password : password of the user

    """

    email: EmailStr
    password: str


class user_update(BaseModel):
    """
    This pydantic model represents the input data to needed to update user information in firestore

    Attributes:
        email : emailid of the user # this field is optional
        full_name : full_name of the user # this field is optional
        username : username of the user # this field is optional

    """

    email: Optional[
        EmailStr
    ] = None  # Optional: Can be left empty to keep existing email.
    full_name: Optional[
        str
    ] = None  # Optional: Can be left empty to keep existing full name.
    username: Optional[
        str
    ] = None  # Optional: Can be left empty to keep existing username.


class reset_password(BaseModel):
    """
    This pydantic model represents the input data to needed to update user password in firebase authentication

    Attributes:
        new_password : users new password

    """

    new_password: str
