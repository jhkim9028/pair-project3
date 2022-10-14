from django.contrib.auth.forms import UserCreationForm

# from accounts.models import User
# from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'password1', 'password2'
        )