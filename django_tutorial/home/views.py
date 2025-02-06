from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("home")
def about(request):
    return HttpResponse("about page")
def booking(request):
    return HttpResponse("booking page")
def doctors(request):
    return HttpResponse("doctors")
def contact(request):
    return HttpResponse("contact")