from django.shortcuts import render, redirect
from .forms.registerForm import *
from .forms.registerForm import UserRegistrationForm

def register_request(request): 
    form = UserRegistrationForm()

    if request.method == 'POST': 
        form = UserRegistrationForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            form.save()
            return redirect("homepage")
    
    else: 
        return render(request, 'register.html', {"form":form, "message":"Invalid data, please try again"})
    
    return render(request, 'register.html', {"form": form})