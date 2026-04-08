from django.shortcuts import render

from django.http import HttpResponse

def login_view(request):
    return HttpResponse("Страница входа (будет позже)")

def signup_view(request):
    return HttpResponse("Страница регистрации (будет позже)")

def profile_view(request):
    return HttpResponse("Страница профиля (будет позже)")