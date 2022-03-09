from django.urls import path
from . import views

urlpatterns = [
    path("cform", views.cform, name="cform"),  
]