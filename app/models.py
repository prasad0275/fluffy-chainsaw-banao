from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import validators
from django.contrib.auth.password_validation import validate_password

# Create your models here.
User = get_user_model()
# This models will contain type of user. e.g Patient or Doctor
class Profile_Type(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return self.type

class Profile(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=256,validators=[validate_password])
    user_type = models.ForeignKey(Profile_Type,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    email = models.EmailField(max_length=128)

    def __str__(self):
        return self.username

class Address(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    house_details = models.CharField(max_length=512)
    street = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    state = models.CharField(max_length=512)
    pincode = models.CharField(max_length=512)

    def __str__(self):
        return self.user






