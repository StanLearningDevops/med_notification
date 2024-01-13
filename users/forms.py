from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',
                'phone_number',)
        
    
class CustomLoginForm(AuthenticationForm):
    
    class Meta(AuthenticationForm):
        model = CustomUser
        fields = ('email', )