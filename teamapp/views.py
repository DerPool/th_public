from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from decimal import Decimal
from .models import Vacancy
from .models import TagAssign, Otklik
from django.contrib.auth.decorators import login_required
from users.models import User,  CustomerProfile
# Create your views here.
import datetime
from django.views.generic import CreateView
from django.db import transaction
from django.views.generic import DetailView, ListView
from .models import Otklik
class IndexView(View):
	profile =  None

	def get(self, request, *args, **kwargs):
		tod = {}
		if request.user is None:
			print("User is NONE")
			tod['profile'] = None
			tod['otkls'] = None
			tod['vacancies']= Vacancy.objects.all()
		else:
			print(request.user.username)
			try:
				self.profile = CustomerProfile.objects.select_related().get(user = request.user.id)
			except ObjectDoesNotExist:
				self.profile = None
			tod['profile'] = self.profile
			tod['vacancies']= Vacancy.objects.all()
			otkls = Otklik.objects.filter(target_user__username=request.user.username)
			if otkls:
				tod['otkls'] = otkls
			else:
				tod['otkls'] = None
			tod['tags']  = TagAssign.objects.all()
			
		return render(request, 'index.html',tod)



class VacancyDetail(DetailView):
	template_name = 'vac_detail.html'
	model = Vacancy



class SearchView(View):
	def get(self, request, *args, **kwargs):
		try:
			vacancies = Vacancy.objects.get(desc__icontains=args[0])
		except ObjectDoesNotExist:
			vacancies = None
		tags  = TagAssign.objects.all()
		return render(request, 'index.html', {'vacancies': vacancies,
			"tags": tags})


class VacancyCreation(View):
	def get(self, request, *args, **kwargs):
		print("Nothing")
		return rediret("/")

	@transaction.atomic
	def post(self, request, *args, **kwargs):
		short_desc = request.POST.get('short_desc', "")
		desc = request.POST.get('desc', "")
		if len(short_desc) < 3 or len(desc) < 10:
			return redirect("/")
		dateofcreation = datetime.datetime.now()
		status = "O"
		newVac = Vacancy.objects.create(
			creator=CustomerProfile.objects.get(user__username =request.user.username),
			desc=desc,
			short_desc=short_desc,
			dateofcreation=dateofcreation,
			status=status)
		newVac.save()
		return redirect("/")


class OtklikView(View):

	@transaction.atomic
	def get(self, request, id, *args, **kwargs):
		prof = CustomerProfile.objects.get(user=request.user)
		targ = Vacancy.objects.get(pk=int(id))
		if targ.creator.user.username == request.user.username:
			return redirect("/")
		otkl = Otklik.objects.create(user=prof, target=targ, date=datetime.datetime.now(), target_user=targ.creator.user, status="P")
		otkl.save()
		return redirect("/")