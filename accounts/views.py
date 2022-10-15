from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def main(request):
    return render(request, "accounts/main.html")


@login_required
def index(request):
    users = get_user_model().objects.all()
    return render(
        request,
        "accounts/index.html",
        {
            "users": users,
        },
    )


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:main")
    else:
        form = CustomUserCreationForm()
    return render(
        request,
        "accounts/signup.html",
        {
            "form": form,
        },
    )


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "accounts:main")
    else:
        form = AuthenticationForm()
    return render(
        request,
        "accounts/login.html",
        {
            "form": form,
        },
    )


@login_required
def detail(request, pk):
    return render(request, "accounts/detail.html")


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(
        request,
        "accounts/update.html",
        {
            "form": form,
        },
    )


@login_required
def logout(request):
    auth_logout(request)
    return redirect("accounts:main")
