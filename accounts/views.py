from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not  None:
            auth.login(request,user)
            messages.success(request,"Welcome To Dashboard")
            return redirect("dashboard")
        else:
            messages.error(request,"Invalid Username or Password")
        return redirect("login")
    return render(request,"accounts/login.html")
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username Already Exists")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email Already Exists")
                    return redirect("register")
                else:
                    user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                    messages.success(request,"Registered Successfully!!!")
                    user.save()
                    # code For auto login user
                    # auth.login(request,user)
                    # messages.success(request,"Your now logged in!")
                    return redirect("login")
        else:
            messages.error(request,"Password and Confirm Password does not match...")
            return redirect("register")
    return render(request,"accounts/register.html")
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect("index")
def dashboard(request):
    user_contacts = Contact.objects.order_by("-contact_date").filter(user_id=request.user.id)
    context = {
        "contacts": user_contacts
    }
    return render(request,"accounts/dashboard.html",context)