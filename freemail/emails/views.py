from django.shortcuts import render,HttpResponse,redirect
from emails.models import Members,Ymail
import random,string
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
# Create your views here.
oid=str(random.randrange(1000,9999))
def ulogin(request):
    if request.method =='GET':
        return render(request,'login.html')
    else:
        vname=request.POST['uname']
        vemail=request.POST['uemail']        
        m=Members.objects.create(name=vname,email=vemail,code=oid)
        m.save()
        msg="Your Verfication code is: "+oid
        print(msg)
        send_mail(
            "Account Verification",
            msg,
            "ppanaskar9@gmail.com",
            [vemail],
            fail_silently=False,        
        )
        return render(request,'otp.html')
    
def eotp(request,rid):
    context={}
    if request.method == 'GET':
        return render (request,'otp.html')
    else:
        a=Members.objects.filter(id=rid)
        votp=request.POST['wotp']
        m=authenticate(code=votp)
        print(a)
        if m is not None:
            login(request,m)
            return render(request,'msg.html')
        else:
            context['error']="Invalid OTP"
            return render(request,'otp.html',context)
        
def msg(request):
    if request.method =='GET':
        return render(request,'msg.html')
    else:
        vmsg=request.POST['umsg']
        demail=request.POST['uemail']
        y=Ymail.objects.create(receiver=demail,msg=vmsg)
        y.save()
        send_mail(
            "FreeMails",
            vmsg,
            "ppanaskar9@gmail.com",
            [demail],
            fail_silently=False,        
        )
        return HttpResponse("Your Message was Sent!!!")


