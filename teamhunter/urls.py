"""teamhunter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from teamapp.views import IndexView, VacancyDetail, SearchView, VacancyCreation, OtklikView
from users.views import SignUpView, CustomerSUView, LogoutView,LoginView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="home"),
    path('vacancy/<int:pk>/', VacancyDetail.as_view(), name='vac-detail'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('search/<slug:string>/', SearchView.as_view()),
    path('account/signup', SignUpView.as_view(), name="signup"),
    path('account/signup/customer', CustomerSUView.as_view(), name="Csignup"),
    path('account/logout', LogoutView.as_view(), name="logout"),
    path('account/login', LoginView.as_view(), name="login"),
    path("vacancy/create/", VacancyCreation.as_view(), name='vCreate'),
    path("otkl/<id>/", OtklikView.as_view(), name="otkl")

]
