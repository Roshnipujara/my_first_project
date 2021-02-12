from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Login,Doctor,Rating,gallery


# class userform(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=["u_name","u_email","u_password","u_number","u_address"]


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=["rating","d_id","date","r_desc"]

class GalleryForm(forms.ModelForm):
    g_path=forms.FileField()
    class Meta:
        model=gallery
        fields=['g_path']


