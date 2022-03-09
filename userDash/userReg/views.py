from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import MyForm


# Create your views here.

# def login(request):
#     if request.method =='POST':
#         phoneNo = request.POST['phoneNo']
#         password= request.POST['dob']

#         print(password)
        

#         user = auth.authenticate(phoneNo=phoneNo, password=password)
        
#         if user is not None:
#             auth.login(request, user)

#             print(user.UserType)

#             if user.UserType == 'student':
#                 return render(request, "student.html")
#             if user.UserType == 'parent':
#                 return render(request, "parent.html")
#             if user.UserType == 'teacher':
#                 return render(request, "teacher.html")

#             return render(request, "student.html")


#         else:
#             messages.info(request,'invalid credentials')
#             return redirect('login')
#     else:
#         return render(request, "login.html")


def login(request):
    if request.method =='POST':
        phoneNo = request.POST['phoneNo']
        password= request.POST['dob']

        print(password)

        form=MyForm(request.POST)
        if form.is_valid():
            print("success")
            messages.success(request,"Valid Captcha!")
        else:
            print("fail")
            messages.error(request,"Invalid Captcha!")
            return redirect('login')
        

        user = auth.authenticate(phoneNo=phoneNo, password=password)
        
        if user is not None:
            auth.login(request, user)

            print(user.UserType)

            if user.UserType == 'student':
                return render(request, "student.html")
            if user.UserType == 'parent':
                return render(request, "parent.html")
            if user.UserType == 'teacher':
                return render(request, "teacher.html")

            return render(request, "student.html")


        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        form=MyForm()
        return render(request, "login.html", {"form":form})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phoneNo = request.POST['phoneNo']
        dob = request.POST['dob']
        UserType = request.POST.get('UserType')

        User = get_user_model()

        user = User.objects.create_user(first_name=first_name, last_name=last_name, phoneNo=phoneNo, dob=dob, UserType=UserType, password=dob)
        user.save()
        return redirect('login')


    else:
        return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')       