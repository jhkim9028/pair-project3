from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from accounts.models import User
# from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'password1', 'password2'
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'email'
        )