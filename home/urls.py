from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('ttt/',include('ttt.urls')),
    path('phonebook/',include('phonebook.urls'))
]