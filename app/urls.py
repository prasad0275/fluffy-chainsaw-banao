from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    # path('signup?dest=home',views.signup),
    # path('signup?dest=form',views.signup),
    path('logout',views.logout), 
    path('login',views.login,name="login")


]