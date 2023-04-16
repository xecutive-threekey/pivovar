from django.shortcuts import render
from django.http import HttpResponse

def register_page(request):
    context = {}
    return render(request, 'account/register.html', context)


def login_page(request):
    context = {}
    return render(request, 'account/login.html', context)


def home(request):
    return HttpResponse('Домашняя страница проекта')