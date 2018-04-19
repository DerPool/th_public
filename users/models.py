from django.db import models
from teams.models import Tag
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="base_user")
    name = models.CharField(max_length=15, default="Unknown")
    surname = models.CharField(max_length=30, default="Unknown")
    fathername = models.CharField(max_length=20, default="Unknown")
    dateofbirth = models.DateField(default = datetime.date.today)
    place = models.CharField(max_length = 20, default="Unknown")
    country = models.CharField(max_length=20, default="Unknown")
    phonenumber = models.CharField(max_length=12, default="Unknown")
    email = models.EmailField()
    decription = models.CharField(max_length=500, default="Unknown")

    def __str__(self):
    	return self.surname + " " + self.name + " " + self.fathername


class CompanyProfile(models.Model):
	pass
