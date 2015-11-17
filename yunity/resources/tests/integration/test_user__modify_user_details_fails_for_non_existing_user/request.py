from .initial_data import request_user

request = {
    "endpoint": "/api/users/12345",
    "method": "put",
    "user": request_user,
    "body": {
        "display_name": "My brand new name",
    }
}
