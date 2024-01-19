# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ObtainTokenSerializer
from .models import AuthToken
import uuid


class CustomAuthView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ObtainTokenSerializer
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        token = request.data.get("token")

        user = authenticate(request, username=username, email=email, password=password, token=token)
        if user is not None:
            login(request, user)
            try:
                auth_token = AuthToken.objects.get(user=user)
                auth_token.token = uuid.uuid4()
                auth_token.save()
            except AuthToken.DoesNotExist:
                auth_token = AuthToken.objects.create(user=user, token=uuid.uuid4())
            return Response({'detail': 'Authentication successful', 'token': auth_token.token}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
