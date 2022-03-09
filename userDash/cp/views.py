from django.contrib import messages
from django.shortcuts import render
from .forms import MyForm

# Create your views here.
def cform(request):
   if request.method=="POST":
      form=MyForm(request.POST)
      if form.is_valid():
         print("success")
         messages.success(request,"Valid Captcha!")
      else:
         print("fail")
         messages.error(request,"Invalid Captcha!")

   form=MyForm()
   return render(request,"form.html",{"form":form})