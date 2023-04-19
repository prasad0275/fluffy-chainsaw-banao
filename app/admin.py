from django.contrib import admin
from .models import Profile_Type,Profile,Address
# Register your models here.
@admin.register(Profile_Type)
class Profile_TypeAdmin(admin.ModelAdmin):
    list_display = ['id','type']

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ['id','user','user_type','profile_picture']

@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display = ['id','house_details','street','city','state','pincode']