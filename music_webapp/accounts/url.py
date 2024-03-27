from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('forgot-username/', views.forgot_username_view, name='forgot_username'),
    # Add more URL patterns as needed
]
