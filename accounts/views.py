from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy 
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
class SignUpView(generic.CreateView): 
    form_class =  CustomUserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'signup.html'
#User = get_user_model()

# Create your views here.
