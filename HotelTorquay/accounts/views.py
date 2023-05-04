from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .forms import ProfileForm

# Create your views here.
class profile_view(DetailView):
    model = UserProfile
    template_name= 'profile.html'
    context_object_name = 'profile'

class signup_view(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'