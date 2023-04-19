from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages,auth
from .models import Profile_Type,Profile,Address
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/login')
def index(request):
    user_model = User.objects.get(username=request.user)
    profile_model = Profile.objects.get(user=user_model)
    address_model = Address.objects.get(user=user_model)
    print(request.user)
    print(user_model.first_name)
    print(profile_model.profile_picture.path)
    return render(request,"index.html",{'user_model':user_model,'profile_model':profile_model,'address_model':address_model})

def signup(request):
    dest = {}
    if request.method == 'GET':
        dest = request.GET.get('dest')
    if request.GET.get("dest") == None:
        if request.method == 'POST':
            user_type = request.POST.get('utype')
            return redirect('/signup?dest=form&type='+user_type)
    
    if request.GET.get("dest") == 'form' :
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            profile_picture = request.FILES.get('profile_picture')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            con_passowod = request.POST.get('con_password')
            house_details = request.POST.get('house_details')
            street = request.POST.get('street')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            type = request.GET.get('type')
            # print(request.data)

            if password != con_passowod:
                messages.info(request,"Password Mismatch!")
                return redirect('/signup?dest=form&type='+type)
            
            elif(User.objects.filter(email = email).exists()):
                messages.info(request,'Email is already exists!')
                return redirect('signup')
        
            elif(User.objects.filter(username = username).exists()):
                messages.info(request,'Username is already taken!')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()

                profile = Profile.objects.create(
                    user=user,
                    user_type=Profile_Type.objects.get(type=type),
                    profile_picture = profile_picture
                )
                profile.save()

                address = Address.objects.create(
                    user = user, 
                    house_details = house_details,
                    street=street,
                    city=city,
                    state=state,
                    pincode=pincode
                )
                address.save()
                messages.info(request,"Register Successfully!")
                return redirect('/login')
        
    return render(request,"signup.html",{'dest':dest})

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print("logout")
        return redirect('/')
    return render(request,"signup.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username," ",password)
        # user_model = User.objects.get(username=username)
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            user_model = User.objects.get(username=username)
            profile_model = Profile.objects.get(user=user_model)
            address_model = Address.objects.get(user=user_model)
            print("login successfully")
            print(user_model.first_name)
            print(profile_model.profile_picture)
            # messages.info(request,"Login successfully")
            return redirect('/',{'user_profile':user_model,'profile_model':profile_model,'address_model':address_model})
        else:
            messages.info(request,'Invalid Credentials')
            print("not login")
            return redirect('/login')
    return render(request,"login.html")