import sys

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from knock_knock import settings
from .forms import RatingForm
from .models import Login,Rating
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Doctor,Rating,Login
from datetime import date

from django.core.mail import send_mail
import random

# Create your views here.


def Rate(request):
    rate = Rating.objects.all()
    return render(request, "rating.html",{"rate":rate})


def add_desc(request):
    if request.method == "POST":
        des = request.POST.get('description')
        did = request.POST['did']
        d = date.today()
        if 'admin_id' in request.session:
            v = request.session['admin_id']
            obj = Rating.objects.filter(l_id = v).count()
            if obj == 1:
                try:
                    obj1 = Rating.objects.filter(l_id_id = v).update(r_desc=des ,d_id_id=did ,date=d)
                    obj1.save()
                except:
                    print("-------------------",sys.exc_info())
            else:
                de = Rating(r_desc=des,d_id_id=did,date=d ,l_id_id=v)
                de.save()
            return redirect('/rate')
    else:
        return render(request, "rating.html")


@csrf_exempt
def add_rating(request):
    if request.method == "POST":
        val = request.POST.get('rating')
        did = request.POST.get('did')
        d = date.today()
        print("------+++++++++" , 'admin_id' in request.session)
        if 'admin_id' in request.session:
            v = request.session['admin_id']
            obj = Rating.objects.filter(l_id = v).count()
            print("------------",v)
            print("------------",obj)
            if obj == 1:
                print("Inside If statement")
                try:
                    obj1 = Rating.objects.filter(l_id_id = v).update(rating=val ,d_id_id=did ,date=d)
                    obj1.save()
                except:
                    print("-------------------",sys.exc_info())
            else:
                s = Rating(rating=val, d_id_id=did, date=d, l_id_id=v)
                s.save()
            return render(request, "add_rating.html", {'val': val})
    else:
        return render(request, "add_rating.html")




def index(request):
    return render(request, "home.html")


def logout_req(request):
    logout(request)
    messages.info(request, "logout successfully")
    return redirect("home.html")


def forget_password(request):
    return render(request, "forgot-password.html")


def loginpage(request):
    if request.method == "POST":
        e = request.POST['email']
        p = request.POST['password']

        val = Login.objects.filter(l_email=e, l_password=p)

        if val:
            data = Login.objects.filter(l_email=e ,l_password=p)
            for item in data:
                request.session['admin_id']=item.l_id
                request.session['admin_email']=item.l_email
                request.session['admin_password']=item.l_password

            if request.POST.get("remember"):
                response = HttpResponse
                response.set_cookie('cemail', request.POST["email"])
                response.set_cookie('cpass', request.POST["password"])
                return response
            return redirect("/rate/")
        else:
            messages.error(request,"Invalid Username or Password")
            return render(request, "login.html")
    else:
        if request.COOKIES.get("cemail"):
            return render(request, "home.html",
                          {'cookie1': request.COOKIES['cemail'], 'cookie2': request.COOKIES['cpass']})
        else:
            return render(request, "login.html")


def scookie(request):
    response = HttpResponse("cookie example")
    response.set_cookie('cid', 'abc@gmail.com')
    return response


def gcookie(request):
    a = request.COOKIES['cid']
    return HttpResponse("value is" + a)


def send_OTP(request):
    otp1 = random.randint(100000,999999)
    e=request.POST['email']
    #request.session['temail']=e
    obj=Login.objects.filter(l_email = e)

    if obj:
        val = Login.objects.filter(l_email=e).update(otp=otp1 , otp_used=0)
        subject='OTP verification'
        message =str(otp1)
        email_from=settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail(subject, message, email_from ,recipient_list)
        return render(request,'home.html')