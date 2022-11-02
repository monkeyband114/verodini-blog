from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'bio', 'name', 'username', 'email']
        
        
class MyUserStartForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
