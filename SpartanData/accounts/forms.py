from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .RegAnalysis import RegularAnalysisMethods
#from .PredAnalysis import

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class UploadDataForm():
    uploaded_file = forms.CharField(max_length=100, help_text='Last Name')
    #regAnalysis = RegularAnalysisMethods(uploaded_file)
    #predAnalysis = PredictiveAnalysisMethods(uploaded_file)
