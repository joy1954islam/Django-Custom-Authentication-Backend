# urls.py
from django.urls import path
from .views import CustomAuthView

urlpatterns = [
    path('api/token/', CustomAuthView.as_view(), name='api-token'),
    # Add more authentication endpoints as needed
]
