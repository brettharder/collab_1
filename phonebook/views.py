from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Contact 

# Create your views here.
def phonebook(request):
    print(request.POST)
    contacts= Contact.objects.all()
    content={'contacts':contacts}
    return render(request, "phonebook/phonebook.html",content)