from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
def ttt(request):
    return render(request, "ttt/ttt.html")

