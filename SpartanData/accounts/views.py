from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from pandas.api.types import is_numeric_dtype
import pandas as pd

from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .tokens import account_activation_token

from .forms import UploadDataForm


def home_view(request):
    return render(request, 'login_home.html')

def login_home_view(request):
    return render(request, 'home.html')

def activation_sent_view(request):
    return render(request, 'activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('/login')
    else:
        return render(request, 'activation_invalid.html')

def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                #login(request, user)
                #messages.info(request, f"You are now logged in as {username}")
                return redirect('/home')
            else:
                return redirect('/signup')
        else:
            return redirect('/signup')
    form = AuthenticationForm()
    return render(request = request,
                    template_name = 'login.html',
                    context={'form':form})

def check_dtype(attr_index):
    attributes = attribute_list()
    if is_numeric_dtype(df[attributes[attr_index]]):
        return True
    else:
        return False

def dashboard(request):
    if request.method == 'POST':
        #if user.profile.upload_confirmation:
        #    print('hi')
        #else:
            uploaded_file = request.FILES['document']
            last_chars = uploaded_file.name[-3:]
            try:
                if last_chars != 'csv' or uploaded_file.size < 1:
                    raise Exception('Invalid Uploaded File. Make sure it is a csv file.')
                df = pd.read_csv(uploaded_file)
                print(uploaded_file.name)
                print(uploaded_file.size)
            except:
                return redirect('Invalid Uploaded File. Make sure it is a csv file.')
            # Assuming upload sucessful
            #user.profile.upload_confirmation = True
            #user.save()
    return render(request, 'dashboard.html')
