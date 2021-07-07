from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('accounts/change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html', success_url='done'),  name='change-password'),
    path('accounts/change-password/done', auth_views.PasswordChangeDoneView.as_view(template_name='registration/change-password-done.html'), name="change-password-done"),
    path('accounts/reset-password', auth_views.PasswordResetView.as_view(template_name='registration/reset-password.html', success_url="done"), name="reset-password"),
    path('accounts/reset-password/done', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset-password-done.html'), name="reset-password-confirm"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
