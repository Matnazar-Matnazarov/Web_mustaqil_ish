from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail





class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default="profile_picture.jpg")
    
    
