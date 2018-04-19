from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import CustomerProfile, User
from teamapp.models import Tag



class CustomerSUForm(UserCreationForm):
	name = forms.CharField()
	surname = forms.CharField()
	fathername = forms.CharField()
	dateofbirth = forms.DateField(widget=forms.SelectDateWidget(years= range(1950, 2003)))
	country  = forms.CharField()
	city = forms.CharField()
	email = forms.EmailField(widget=forms.EmailInput)



	class Meta(UserCreationForm.Meta):
		model  = User

	@transaction.atomic
	def save(self):
		user  = super().save(commit=False)
		user.is_customer = True
		user.save()
		customer = CustomerProfile.objects.create(user=user)
		customer.name = self.cleaned_data.get("name")
		customer.surname = self.cleaned_data.get("surname")
		customer.fathername = self.cleaned_data.get("fathername")
		customer.dateofbirth = self.cleaned_data.get("dateofbirth")
		customer.city = self.cleaned_data.get("city")
		customer.country = self.cleaned_data.get("country")
		customer.email = self.cleaned_data.get("email")
		customer.save()
		return user
