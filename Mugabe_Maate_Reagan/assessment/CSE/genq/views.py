from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import User_account

# Create your views here.
def kyc_form(request):
    return render(request,'kyc.html')

def kyc_details(request):
    name1=type(str)
    name2=type(str)
    name1 = request.POST.get['fname']
    name2=request.POST['lname']
    birthday=request.POST.get['DOB']
    sex=request.POST.get['gender']
    states=request.POST.get['LOCATION']
    city = request.POST.get['vtown']
    codeblock=request.POST.get['icode']
    phone1=request.POST.get['phone1']
    phone2=request.POST.get['phone2']
    iemail=request.POST.get['email']
      
    if User.objects.filter(fname=name1,lname=name2,
                           DOB=birthday,gender=sex,
                           LOCATION=states,email=iemail,
                           phone2=phone2,phone1=phone1,
                           icode=codeblock,state=city).first():
     
        user_account=User.objects.create_user(name1, name1, birthday,sex,
                                              states,city,codeblock,phone1,
                                              phone2,iemail )
                                              
        
    return render(request, 'kyc.html')
              
