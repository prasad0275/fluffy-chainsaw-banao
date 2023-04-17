from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
# Create your views here.

@login_required(login_url='/login')
def index(request):
    return render(request,"index.html")

def signup(request):
    dest = {}
    type = None
    first_name = None
    last_name = None
    profile_picture = None
    username = None
    email = None
    password = None
    con_passowod = None
    house_details = None
    street = None
    city = None
    state = None
    pincode = None

    print(request.path)

    if request.method == 'GET':
        dest = request.GET.get('dest')
        print(dest)
        print(request.path)
    
    if request.GET.get("dest") == None:
        if request.method == 'POST':
            type = request.POST.get('type')
            # print(type)
            return redirect('/signup?dest=form')
    
    if request.GET.get("dest") == 'form':
        print("into form")
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            profile_picture = request.POST.get('profile_picture')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            con_passowod = request.POST.get('con_password')
            house_details = request.POST.get('house_details')
            street = request.POST.get('street')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            if password != con_passowod:
                messages.info(request,"Pass Mismatch!")
            
            print("form details")
        
    return render(request,"signup.html",{'dest':dest,})

def signup_home(request):
    if request.method == 'POST':
        print('home post')
        return redirect('/signup')

def signup_form(request):
    if request.method == 'POST':
        print('form post')
def login(request):
    return render(request,"")