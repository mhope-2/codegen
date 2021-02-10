from django.shortcuts import render, redirect
import requests 
import uuid
import random
from random import shuffle
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import logging
from django.conf import settings

logging.basicConfig(filename=str(settings.BASE_DIR) + '/logs/smslog.logs',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    level=logging.DEBUG)

# Create your views here.
def index(request):

    # return render(request, 'accounts/register.html')

    return render(request, 'index.html')


