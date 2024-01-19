
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import AuthToken
UserModel = get_user_model()

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, password=None, token=None, **kwargs):
        # Authenticate using username/password
        if username and password:
            user = UserModel.objects.filter(username=username).first()
            if user and user.check_password(password):
                return user

        # Authenticate using email/password
        if email and password:
            user = UserModel.objects.filter(email=email).first()
            if user and user.check_password(password):
                return user

        # Authenticate using token
        if token:
            # Assume you have a model named AuthToken with a field 'token'
            auth_token = AuthToken.objects.filter(token=token).first()
            if auth_token and not auth_token.is_expired():
                return auth_token.user

        # Return None if no valid user is found
        return None

