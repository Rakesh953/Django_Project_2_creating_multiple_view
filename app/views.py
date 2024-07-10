from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def srujana(request):
    return HttpResponse('<h1><marquee>Hey This is Srujana</marquee></h1>')

def rama(request):
    return HttpResponse('<h1><marquee>Hey This is Rama</marquee></h1>')