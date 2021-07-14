from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from siteusers.views import dashboard, register 


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register")
]
