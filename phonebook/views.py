from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic

from .models import Contact 

import json

# Create your views here.
def phonebook(request):
    if(request.POST):
        if(request.POST.get("newContactName1")):
            name=request.POST.get("newContactName1")
            if(request.POST.get("newContactNumber1")):
                number=request.POST.get("newContactNumber1")
                contact=Contact(name=name,number=number)
                contact.save()
        if(request.is_ajax):
            print("its ajax")
            if(request.POST.get('newContactName2')):
                name=request.POST.get("newContactName2")
                if(request.POST.get("newContactNumber2")):
                    number=request.POST.get("newContactNumber2")
                    contact=Contact(name=name,number=number)
                    contact.save()
    if(request.GET.get('deleteContact')):
        tid=request.GET.get('deleteContact')
        contact=Contact.objects.get(id=tid)
        contact.delete()
    contacts= Contact.objects.all()
    content={'contacts':contacts}
    return render(request, "phonebook/phonebook.html",content)