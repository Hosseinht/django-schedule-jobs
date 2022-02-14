from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
        UserProfile model extends the built-in User model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "User Profiles"
        ordering = ["id"]
