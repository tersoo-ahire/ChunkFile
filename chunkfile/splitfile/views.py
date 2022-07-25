from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# import created forms from forms.py
from splitfile.forms import SignUpForm, SignInForm, CsvFileForm, JsonFileForm


# Create your views here.
def home_view(request):
    return render(request, "index.html")


def about_view(request):
    return render(request, "about.html")


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            user = authenticate(email=email,username=username,password1=password1,password2=password2)
            login(request,user)
            return redirect("dashboard")
        else:
            form = SignUpForm()
            return render(request,"signup.html",{"form":form})

    else:
        form = SignUpForm()
        return render(request,"signup.html",{"form":form})


def signin_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email,password=password)
            login(request,user)
            return redirect("dashboard")
        else:
            form = SignInForm()
            return render(request,"signin.html",{"form":form})

    else:
        form = SignInForm()
        return render(request,"signin.html",{"form":form})


def signout_view(request):
    logout(request)
    return redirect("home")


@login_required(login_url= "signup")
def dashboard_view(request):
    return render(request, "dashboard.html")


@login_required(login_url= "signup")
def splitcsv_view(request):
    form = CsvFileForm()
    form.save()
    return render(request, "splitcsv.html", {"form":form})


@login_required(login_url= "signup")
def splitjson_view(request):
    form = JsonFileForm()
    form.save()
    return render(request, "splitjson.html", {"form":form})


def privacy_policy_view(request):
    return render(request, "privacypolicy.html")


def terms_of_service_view(request):
    return render(request, "termsofservice.html")