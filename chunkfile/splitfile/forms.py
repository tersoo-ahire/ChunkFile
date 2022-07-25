# import form class from django
from django import forms

# import default django form for creating a user
from django.contrib.auth.forms import UserCreationForm

# import default django user model
from django.contrib.auth.models import User

# import created models from models.py
from splitfile.models import CSVFile, JSONFile


# create a ModelForm  
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
        
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")

class SignInForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ("email", "password")
      
class CsvFileForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = CSVFile
        fields = "__all__"
        
        
class JsonFileForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = JSONFile
        fields = "__all__"