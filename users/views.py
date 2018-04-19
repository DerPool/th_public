from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.views.generic import FormView, RedirectView, DetailView
from django.views import View
from .forms import CustomerSUForm
from .models import User, CustomerProfile
# Create your views here.


class SignUpView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'register.html', {})


class CustomerSUView(FormView):
	model = User
	form_class = CustomerSUForm
	template_name = "register/cust_su.html"
	success_url = "/"

	def get_context_data(self, **kwargs):
		kwargs["user_type"] = "customer"
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return super(CustomerSUView, self).form_valid(form)


class LogoutView(RedirectView):
	url = '/'

	def get(self, request, *args, **kwargs):
		logout(request)
		return super(LogoutView, self).get(request, *args, **kwargs)


class LoginView(View):
	def get(self, request):
		if request.user.is_authenticated:
			return redirect("/")
		return render(request, "login.html", {})

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
		else:
			return redirect("/account/login")

		return redirect("/")


class ProfileView(DetailView):
	model = CustomerProfile
	template_name = 'profile.html'