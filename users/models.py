from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    description = models.CharField(max_length=30, blank=True)

    def get_profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return None

    def __str__(self):
            return self.username


