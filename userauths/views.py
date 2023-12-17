from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.conf import settings
from userauths.models import User
from django.contrib.auth.decorators import login_required


# User = settings.AUTH_USER_MODEL

# Create your views here.

def register_view(request):
     
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username} ,Your account was created succesfully")
            new_user =authenticate(username=form.cleaned_data['email'],
                                   password=form.cleaned_data['password1']
            )
            login(request,new_user)
            return redirect("core:index")

    else:
        form = UserRegisterForm()

# to access the fields of the form and display it
    context = {
        'form' : form,
    }
    return render(request,"userauths/sign-up.html",context)

def login_view(request):
    if request.method == "POST":
        email =request.POST.get("email")       
        password =request.POST.get("password")


        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in.")
            return redirect("core:index")
        else:
            messages.warning(request, f"User with {email} doesn't exist.You should create an account")
   
    return render(request, "userauths/sign-in.html")


def logout_view(request):
     logout(request)
     messages.success(request, "You logged out.")
     return redirect("userauths:sign-in")



@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if first_name and last_name and email:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            messages.success(request, 'Profile information updated successfully.')

        if current_password and new_password and confirm_password:
            if user.check_password(current_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user) 
                    messages.success(request, 'Password changed successfully.')
                else:
                    messages.error(request, 'New password and confirm password do not match.')
            else:
                messages.error(request, 'Current password is incorrect.')
        return redirect('/user/profile/')
    return render(request, 'userauths/profiles.html', {'user': user,})

def contact(request):
    return render(request, 'userauths/contact.html')