from django.shortcuts import render , redirect
from . froms import RegisterForm , ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm , SetPasswordForm
from django.contrib.auth import authenticate, login , logout , update_session_auth_hash
# Create your views here.
def home(request) : 
    return render(request ,'index.html')

def register(request) : 
    if not request.user.is_authenticated :
        if request.method == 'POST' : 
            form = RegisterForm(request.POST)
            if form.is_valid() : 
                messages.success(request,'Account Create successfully')
                form.save()
                # print(form.cleaned_data)
        else : 
            form = RegisterForm()
        return render(request , './task/register.html' , {'form':form})
    else : 
        return redirect('home')

def user_login(request) : 
    if not request.user.is_authenticated :
        if request.method == 'POST' : 
            form = AuthenticationForm(request=request , data=request.POST)
            if form.is_valid() : 
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username = name , password = user_pass) #data available or not
                if user is not None : 
                    login(request , user)  
                    return redirect('profile')
        else : 
            form = AuthenticationForm()        
        return render(request , './task/login.html' , {'form':form})  
    else : 
        return redirect('profile') #profile
    
def Profile(request) : 
    if request.user.is_authenticated :
        if request.method == 'POST' : 
            form = ChangeUserData(request.POST , instance=request.user)
            if form.is_valid() : 
                messages.success(request,'Account update successfully')
                form.save()
                # print(form.cleaned_data)
        else : 
            form = ChangeUserData(instance=request.user)
        return render(request , './task/profile.html' , {'form':form})
    else : 
        return redirect('register')
    
def user_logout(request) : 
    logout(request)
    return redirect('login')

def pass_change(request) : 
    if request.method == "POST" : 
        form = PasswordChangeForm(user=request.user , data = request.POST) #update pass
        if form.is_valid() : 
            form.save()
            update_session_auth_hash(request , form.user)
            return redirect('profile')
    else : 
        form = PasswordChangeForm(user=request.user)
    return render(request , './task/passchange.html' , {'form':form})

def pass_change2(request) : 
    if request.method == "POST" : 
        form = SetPasswordForm(user=request.user , data = request.POST) #update pass
        if form.is_valid() : 
            form.save()
            update_session_auth_hash(request , form.user)
            return redirect('profile')
    else : 
        form = SetPasswordForm(user=request.user)
    return render(request , './task/passchange.html' , {'form':form})      

def change_user_data(request) : 
    if request.user.is_authenticated :
        if request.method == 'POST' : 
            form = ChangeUserData(request.POST , instance=request.user)
            if form.is_valid() : 
                messages.success(request,'Account update successfully')
                form.save()
                # print(form.cleaned_data)
        else : 
            form = ChangeUserData(instance=request.user)
        return render(request , 'profile.html' , {'form':form})
    else : 
        return redirect('signup')