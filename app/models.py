from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import validate_password

# Create your models here.
User = get_user_model()
# This models will contain type of user. e.g Patient or Doctor
class Profile_Type(models.Model):
    type = models.CharField(max_length=64)

class Profile(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=256,validators=[validate_password])
    user_type = models.ForeignKey(Profile_Type,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    email_id = models.EmailField(max_length=128)
    address = models.TextField()

    



