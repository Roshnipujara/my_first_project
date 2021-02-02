from django.db import models
# Create your models here.


class Login(models.Model):
    l_id = models.AutoField(primary_key=True)
    l_email = models.EmailField(unique=True)
    l_password = models.CharField(max_length=10)
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField()

    class Meta:
        db_table = "login"


class Doctor(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=50)
    d_desc = models.CharField(max_length=100)

    class Meta:
        db_table = "doctor"


class Rating(models.Model):
    r_id = models.AutoField(primary_key=True)
    rating = models.FloatField(default=0)
    d_id = models.ForeignKey(Doctor, default=1,on_delete=models.SET_DEFAULT)
    date = models.DateField()
    r_desc = models.CharField(max_length=100)
    l_id = models.ForeignKey(Login, default=1, on_delete=models.SET_DEFAULT)

    class Meta:
        db_table = "rate"

