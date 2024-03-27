from django.shortcuts import render

# Create your views here.
from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView
from .forms import UserLoginForm, UserRegistrationForm, UserPasswordResetForm

class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserPasswordResetView(auth_views.PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = '/password_reset/done/'



from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        # Example: Check user credentials and log in user
        return redirect('home')  # Redirect to home page after successful login
    else:
        # Render login form template
        return render(request, 'accounts/login.html')

def register_view(request):
    if request.method == 'POST':
        # Handle registration form submission
        # Example: Create a new user account
        return redirect('login')  # Redirect to login page after successful registration
    else:
        # Render registration form template
        return render(request, 'accounts/register.html')

def forgot_password_view(request):
    if request.method == 'POST':
        # Handle forgot password form submission
        # Example: Send password reset email to user
        return redirect('login')  # Redirect to login page after password reset email sent
    else:
        # Render forgot password form template
        return render(request, 'accounts/forgot_password.html')

def forgot_username_view(request):
    if request.method == 'POST':
        # Handle forgot username form submission
        # Example: Send username reminder email to user
        return redirect('login')  # Redirect to login page after username reminder email sent
    else:
        # Render forgot username form template
        return render(request, 'accounts/forgot_username.html')
