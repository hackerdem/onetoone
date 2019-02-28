from django.shortcuts import render
from django.views.generic import DetailView, FormView
from django.db import models
from .models import Profile
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse

class CreateProfileView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password'],
                                        first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        email=data['email']
                                        )
        user.profile.occupation = data['occupation']
        user.profile.location = data['location']
        user.profile.bio = data['bio']
        user.save()

        return HttpResponse('ok')

class DisplayDetailView(DetailView):
    model = Profile
