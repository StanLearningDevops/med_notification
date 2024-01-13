from django. urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from axes.decorators import axes_dispatch
from django.contrib.auth import authenticate

from .forms import CustomUserCreationForm
from .forms import CustomLoginForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'