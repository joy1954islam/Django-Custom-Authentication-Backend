
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid 


class AuthToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        # Customize this method based on your token expiration logic
        # For example, you might want to set an expiration time for tokens
        expiration_time = timezone.now() - timezone.timedelta(days=1)
        return self.created_at < expiration_time
    
    def __str__(self):
        return str(self.token)


