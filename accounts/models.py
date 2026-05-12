from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="profile")
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    image = models.ImageField(upload_to="profile/",default="profile/default.png")
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.name