# Backend_UserManagement_System_with_FastAPI-_and_Firebase
# User Management System with FastAPI, Firebase, and Python Stamps
<p>
  <img src="https://www.python.org/static/community_logos/python-logo.png" width="300" height="350">
  <img src="https://firebase.google.com/images/brand-guidelines/logo-logomark.png" width="350" height="350">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="350" height="350">
</p>

## Introduction

Welcome to the User Management System! This project is a API built with FastAPI and Firebase for authentication and for database interactions. It provides a set of RESTful API endpoints for user registration, user information retrieval, user information update, user deletion, and password reset.

## Installation

### Windows:

1. **Clone the repository:**

    ```powershell
    git clone https://github.com/SHOOTDEAD/Backend_UserManagement_System_with_FastAPI-_and_Firebase.git
    cd Backend_UserManagement_System_with_FastAPI-_and_Firebase
    ```

2. **Create a virtual environment (optional but recommended):**

    ```powershell
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install the required dependencies:**

    ```powershell
    pip install -r requirements.txt
    ```

4. **Configure Firebase:**

    - Create a Firebase project on the Firebase Console (https://console.firebase.google.com/).
    - Set up authentication methods (e.g., email/password) and generate a Firebase Admin SDK private key JSON file.
    - Place that JSON file in the project director
    - Generate API key
    - Copy DatabaseUrl

5. **Path:**

    - Edit the `paths.js` file to configure your Firebase_file_path,API_KEY,DatabaseUrl.

6. **Run the application:**

    ```powershell
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

### Linux (Ubuntu/Debian-based systems):

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SHOOTDEAD/Backend_UserManagement_System_with_FastAPI-_and_Firebase.git
    cd Backend_UserManagement_System_with_FastAPI-_and_Firebase
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Firebase:**

    - Create a Firebase project on the Firebase Console (https://console.firebase.google.com/).
    - Set up authentication methods (e.g., email/password) and generate a Firebase Admin SDK private key JSON file.
    - Place that JSON file in the project director
    - Generate API key
    - Copy DatabaseUrl

5. **Path:**

    - Edit the `paths.js` file to configure your Firebase_file_path,API_KEY,DatabaseUrl.

6. **Run the application:**

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```


The User Management System should now be running locally. You can access it at `http://localhost:8000`.

## API Endpoints

### User Registration

- **Endpoint:** `/Create_user`
- **Method:** `POST`
- **Description:** Register a new user in firebase and store its information in firestore.
- **Request body:** JSON containing user details (email,password,full_name.username).

### Login

- **Endpoint:** `/Login`
- **Method:** `POST`
- **Description:** Authenticate user information and logs user in .


### User Information Retrieval

- **Endpoint:** `/User_info`
- **Method:** `GET`
- **Description:** Retrieve user information by user credentials.

### User Information Update

- **Endpoint:** `/User_info`
- **Method:** `PUT`
- **Description:** Update user information by user ID.
- **Request body:** JSON containing updated user credentials.

### User Deletion

- **Endpoint:** `/Delete_User`
- **Method:** `DELETE`
- **Description:** Delete a user by user credentials.

### Password Reset

- **Endpoint:** `/Reset_password`
- **Method:** `POST`
- **Description:** Reset a user's password.
- **Request body:** JSON containing password reset.

## Acknowledgments

- Thanks to the FastAPI, Firebase communities for their great libraries and tools.
