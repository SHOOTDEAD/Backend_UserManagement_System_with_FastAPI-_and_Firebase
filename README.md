# Backend_UserManagement_System_with_FastAPI-_and_Firebase
# User Management System with FastAPI, Firebase, and Python Stamps
<p>
  <img src="https://www.python.org/static/community_logos/python-logo.png" width="300" height="350">
  <img src="https://firebase.google.com/images/brand-guidelines/logo-logomark.png" width="350" height="350">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="350" height="350">
</p>

## Introduction

Welcome to the User Management System! This project is a web application built with FastAPI, Firebase for authentication, and Python Stamps for database interactions. It provides a set of RESTful API endpoints for user registration, user information retrieval, user information update, user deletion, and password reset.

## Installation

To set up this project on your local machine, follow these steps:

1. **Clone the repository:**

    ```shell
    git clone https://github.com/yourusername/user-management-system.git
    cd user-management-system
    ```

2. **Create a virtual environment (optional but recommended):**

    ```shell
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install the required dependencies:**

    ```shell
    pip install -r requirements.txt
    ```

4. **Configure Firebase:**

    - Create a Firebase project on the Firebase Console (https://console.firebase.google.com/).
    - Set up authentication methods (e.g., email/password) and generate a Firebase Admin SDK private key JSON file.
    - Rename the Firebase Admin SDK private key JSON file to `firebase_credentials.json` and place it in the root directory of the project.

5. **Configuration:**

    - Edit the `config.py` file to configure your Firebase project settings.

6. **Run the application:**

    ```shell
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

The User Management System should now be running locally. You can access it at `http://localhost:8000`.

## API Endpoints

### User Registration

- **Endpoint:** `/register`
- **Method:** `POST`
- **Description:** Register a new user.
- **Request body:** JSON containing user details (e.g., email and password).

### User Information Retrieval

- **Endpoint:** `/user/{user_id}`
- **Method:** `GET`
- **Description:** Retrieve user information by user ID.

### User Information Update

- **Endpoint:** `/user/{user_id}`
- **Method:** `PUT`
- **Description:** Update user information by user ID.
- **Request body:** JSON containing updated user information.

### User Deletion

- **Endpoint:** `/user/{user_id}`
- **Method:** `DELETE`
- **Description:** Delete a user by user ID.

### Password Reset

- **Endpoint:** `/reset-password`
- **Method:** `POST`
- **Description:** Reset a user's password.
- **Request body:** JSON containing user email for password reset.

## Contributing

If you would like to contribute to this project, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the FastAPI, Firebase, and Python Stamps communities for their great libraries and tools.
