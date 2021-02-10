from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
import random
import uuid
#from .permissions import IsAuthorOrReadOnly
from django.views.generic import ListView, TemplateView, CreateView, DetailView, View
from .forms import UserCreateForm
from django.urls import reverse_lazy, reverse
from rest_framework import viewsets # new
from . import forms
from django.contrib.auth import mixins
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count
# Viewing Profile
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import SingleObjectMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

import numpy as np
import pandas as pd
import json

from user_app.models import UserProfile


class HomeView(TemplateView):
    template_name = 'user_app/index.html'


class ProfileView(TemplateView,LoginRequiredMixin):

    login_url = '/user_app/login/'
    redirect_field_name = 'user_app:login'

    model = User
    template_name = 'page-user.html'
    # template_name = 'user_app/login_views/profile_view.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['code'] = ""
        context['first_name'] = self.request.user.first_name
        context['last_name'] = self.request.user.last_name
            

        try:

            if  UserProfile.objects.filter(code__isnull=True):
                
                gen_code = str(self.request.user.first_name)[0] + str(self.request.user.last_name)[0] + str(random.Random(uuid.uuid1().hex).getrandbits(128))[0:6]
                gen_code_save = UserProfile(user=self.request.user, code=gen_code)
                gen_code_save.save()
                context['code'] = UserProfile.objects.values_list('code', flat=True).get(user=self.request.user)
                    
            else:
                context['code'] = UserProfile.objects.values_list('code', flat=True).get(user=self.request.user)
        
        except UserProfile.DoesNotExist as e:
            
                gen_code = str(self.request.user.first_name)[0] + str(self.request.user.last_name)[0] + str(random.Random(uuid.uuid1().hex).getrandbits(128))[0:6]
                gen_code_save = UserProfile(user=self.request.user, code=gen_code)
                gen_code_save.save()
                context['code'] = UserProfile.objects.values_list('code', flat=True).get(user=self.request.user)

        
        return context


    

class SignUpView(CreateView):
    model = User
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('user_app:login')
    template_name = 'accounts/register.html'
    # template_name = 'user_app/registration/sign_up.html'


class LogoutView(TemplateView):
    template_name = 'user_app/registration/logout_success.html'   


def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")

    user.is_verified = True
    user.is_active = True
    user.save()

    return redirect('login')


