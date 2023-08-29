from django.shortcuts import render
from django.views.generic import TemplateView

#! index_view 
def index_view(request):
    return render(request, 'index.html')

class LoginView(TemplateView):
    template_name = 'login.html'

class RegisterView(TemplateView):
    template_name = 'register.html'

class PasswordResetRequestView(TemplateView):
    template_name = 'password_reset_request.html'

class PasswordResetConfirmView(TemplateView):
    template_name = 'password_reset_confirm.html'
