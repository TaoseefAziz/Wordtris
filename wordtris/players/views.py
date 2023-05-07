from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login_player(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        player = authenticate(request, username=username, password=password)
        
        if player is not None:
            login(request, player)
            return redirect('game')
        else: 
            messages.success(request, ('There was an error logging in!'))
            redirect('login')
            return render(request, 'authenticate/login.html',{})
    else:
        return render(request, 'authenticate/login.html',{})
    
def register_player(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            # ignoring password 2 (confirmation field) that is autogenerated
            password = form.cleaned_data['password1']
            
            player = authenticate(username=username, password=password)
            login(request, player)
            messages.success(request, ('Registered successfully!'))
            return redirect('game')
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register.html',{'form':form,})
    
def logout_player(request):
    messages.success(request, ('You were logged out'))
    logout(request)
    return redirect('login')