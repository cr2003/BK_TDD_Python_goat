# lists/views.py (ch03l009)
from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<html><title>To-Do lists</title></html>")

