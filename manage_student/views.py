from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from app.models import CustomUser

from django.contrib.auth.decorators import login_required

def LOGIN(request):
    return render(request, "login.html")


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(
            request,
            email=request.POST.get("email"),
            password=request.POST.get("password"),
        )
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == "1":
                return redirect("hod_home")
            elif user_type == "2":
                return HttpResponse("this is staff panel")
            elif user_type == "3":
                return HttpResponse("this is student panel ")
            else:
                messages.error(request, "Email and password are Invalid !")
                return redirect("login")
        else:
            messages.error(request, "Email and password are Invalid !")
            return redirect("login")


def doLogout(request):
    logout(request)
    return redirect("login")

@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id )
    context = {
        "user" : user,
    }
    return render(request, "profile.html" ,context)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        print(profile_pic)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        #email = request.POST.get("email")
        #username = request.POST.get("username")
        password = request.POST.get("password")
        
        try:
            customeruser = CustomUser.objects.get(id = request.user.id)

            customeruser.first_name = first_name
            customeruser.last_name = last_name
            
            if password != None and password != "":
                customeruser.set_password(password)
            if profile_pic != None and profile_pic != "":
                customeruser.profile_pic = profile_pic
            customeruser.save()
            messages.success(request, 'Your profile updated successfully!!!')
            return redirect("profile")
        except:
            messages.error(request, "Failed To Update Your Profile!!!")
            return redirect('profile')
    return render(request,'profile.html')

