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
from .RegAnalysis import attribute_list, mean, median, mode, csv_json, attribute_list
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .forms import UploadDataForm
from .PredAnalysis import data_prep, rand_forest, k_neighbors, naive_bayes, attribute_list_num

import json

GLOBAL_df = None
GLOBAL_attributes = None
GLOBAL_numerical_attributes = None
GLOBAL_attributes_mean = None
GLOBAL_uploaded_file = None
GLOBAL_pred_analysis_return = None

def home_view(request):
    return render(request, 'login_home.html')

def activated_view(request):
    return render(request, 'activated.html')

def login_home_view(request):
    return render(request, 'home.html')

def activation_sent_view(request):
    return render(request, 'activation_sent.html')

def analysisChoose(request):
    return render(request, 'analysisChoose.html')

def predAnalysis(request):
    global GLOBAL_df, GLOBAL_numerical_attributes, GLOBAL_uploaded_file, GLOBAL_pred_analysis_return
    attributes = GLOBAL_numerical_attributes
    print(attributes)
    uploaded_file = GLOBAL_uploaded_file
    method_object = ''

    if request.method == 'POST':
        arr = request.POST.get('arr')
        GLOBAL_pred_analysis_return = arr
        print(GLOBAL_pred_analysis_return)

    context = {
        'uploaded_file': uploaded_file,
        'attributes': attributes,
        'features': attributes,

    }
    return render(request, 'predAnalysis.html', context)

def output(request):
    global GLOBAL_pred_analysis_return, GLOBAL_df
    df = GLOBAL_df
    variablesString = GLOBAL_pred_analysis_return #string Model Type, 0, 1, 4, 5
    variablesArray = variablesString.split(",",2)
    print(variablesArray)
    modelType = variablesArray[0]
    print(modelType)
    attributeIndex = variablesArray[1]
    attr_index = int(attributeIndex) #Integer index
    print(attr_index)
    variable = variablesArray[2]
    feature_string = variable.split(",")
    features = [int(i) for i in feature_string] #list of features indexes
    print(features)
    output = []

    if request.is_ajax():
        numdf = data_prep(df)
        
        if modelType == "Random Forest":
            print("reached forest")
            output = rand_forest(numdf, attr_index, features)

        if modelType == "KNN Clustering":
            #print("reached Clustering")
            #output = k_neighbors(numdf, attr_index, features)
            output = ["CLUSTER"]

        if modelType == "Naive Bayes":
            #print("reaching Bayes")
            #output = naive_bayes(numdf, attr_index, features)
            output = ["Bayes"]

    return render(request, 'output.html', {'output': output})

def regAnalysis(request):
    global GLOBAL_df, GLOBAL_attributes
    uploaded_file = GLOBAL_df
    attributes = GLOBAL_attributes
    attribute_means = []
    attribute_count = 0
    attribute_medians = []
    attribute_modes = []
    minRange = 1
    maxRange = 100

    for attribute in attributes:
        attribute_means.append(mean(uploaded_file, attribute_count))
        attribute_medians.append(median(uploaded_file, attribute_count))
        attribute_modes.append(mode(uploaded_file, attribute_count))
        attribute_count = attribute_count + 1

    context = {
        'uploaded_file': csv_json(uploaded_file),
        'attributes': attributes,
        'mean': attribute_means,
        'mode': attribute_modes,
        'median': attribute_medians,
        'minRange': minRange,
        'maxRange': maxRange,
    }
    return render(request, 'regAnalysis.html' , context)


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
            mail_subject = 'Activate your SpartanData account.'
            subject = 'Please Activate Your Account'
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect('/sent')
            user.email_user(subject, message)
            return redirect('activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login_view(request)
        return redirect('/activated')
    else:
        return HttpResponse('Activation link is invalid!')

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

def dashboard(request):
    global GLOBAL_df, GLOBAL_attributes, GLOBAL_numerical_attributes
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        last_chars = uploaded_file.name[-3:]
        try:
            if last_chars != 'csv' or uploaded_file.size < 1:
                print(last_chars)
                print(uploaded_file.size)
                redirected = True
                raise Exception('Invalid Uploaded File. Make sure it is a csv file.')
            df = pd.read_csv(uploaded_file)
            GLOBAL_df = df
            attributes = df.columns.values.tolist()
            GLOBAL_attributes = attributes
            GLOBAL_numerical_attributes = attribute_list_num(df)
            GLOBAL_uploaded_file = uploaded_file
            print(GLOBAL_attributes)
            #request.sessions['df'] = df
            #request.sessions['attributes'] = attributes
            print(uploaded_file.name)
            print(uploaded_file.size)
            return redirect('/analysisChoose')
        except:
            return redirect('/dashboardResubmit')
            # Assuming upload sucessful
            #user.profile.upload_confirmation = True
            #user.save()
    return render(request, 'dashboard.html')

def dashboardResubmit(request):
    global GLOBAL_df, GLOBAL_attributes, GLOBAL_numerical_attributes
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        last_chars = uploaded_file.name[-3:]
        try:
            if last_chars != 'csv' or uploaded_file.size < 1:
                print(last_chars)
                print(uploaded_file.size)
                raise Exception('Invalid Uploaded File. Make sure it is a csv file.')
            df = pd.read_csv(uploaded_file)
            GLOBAL_df = df
            attributes = df.columns.values.tolist()
            GLOBAL_attributes = attributes
            GLOBAL_numerical_attributes = attribute_list_num(df)
            GLOBAL_uploaded_file = uploaded_file
            print("attribute: " + GLOBAL_attributes)
            #request.sessions['df'] = df
            #request.sessions['attributes'] = attributes
            print(uploaded_file.name)
            print(uploaded_file.size)
            print(df)
            return redirect('/analysisChoose')
        except:
            return redirect('/dashboardResubmit')
            # Assuming upload sucessful
            #user.profile.upload_confirmation = True
            #user.save()
    return render(request, 'dashboardResubmit.html')

#def dashboardMasterModalSubmit(request):

def dashboardLineModalSubmit(request):
    if request.method == 'POST':
        x_index = int(request.POST.get('x_index'))
        y_index = int(request.POST.get('y_index'))
        df1 = GLOBAL_df.iloc[:,[x_index, y_index]]
        df1['tuple']=list(zip(GLOBAL_df.iloc[:,x_index],GLOBAL_df.iloc[:,y_index]))
        data = df1['tuple'].to_json('line_plot.json',orient='values')
        return HttpResponse(data)
