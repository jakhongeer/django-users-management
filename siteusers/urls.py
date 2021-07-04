from django.urls import path, include
from . import views

urlpatterns = [
    path("acoounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
] 
