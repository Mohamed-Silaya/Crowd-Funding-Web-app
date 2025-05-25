from django.urls import path
from .views import (
    UserRegistrationView,
    ActivateAccountView,
    UserLoginView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    UserProfileView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('activate/<uuid:activation_key>/', ActivateAccountView.as_view(), name='activate'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('request-password-reset/', PasswordResetRequestView.as_view(), name='request-password-reset'),
    path('reset-password/<uuid:reset_key>/', PasswordResetConfirmView.as_view(), name='reset-password'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
