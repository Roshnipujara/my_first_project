"""knock_knock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from First import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # LOGIN
    path('login/',views.loginpage),
    path('forgot/',views.forget_password),
    path('reset/',views.reset_pass),
    path("logout/",views.logout_req),
    path("sendmail/",views.send_OTP),

    path('scookie/',views.scookie),
    path('gcookie/',views.gcookie),
    path('oauth/', include('social_django.urls', namespace='social')),


    # ######################### StarRating
    path("add_rating/",views.add_rating,name="add_rating"),
    path('rate/',views.Rate,name="rate"),
    path('add_desc/',views.add_desc,name="add_desc"),

    path("gallery_insert/",views.gallery_insert),
    path("",views.blog_view,name='blog'),
    path("<int:id>",views.detail_view,name='details'),


    path("home/",views.index),
    path('header/',views.header),

]
