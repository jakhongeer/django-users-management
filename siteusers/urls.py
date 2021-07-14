from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from siteusers.views import dashboard, register 


urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('accounts/change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html', success_url='done'),  name='change-password'),
    path('accounts/change-password/done', auth_views.PasswordChangeDoneView.as_view(template_name='registration/change-password-done.html'), name="change-password-done"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register")
]
