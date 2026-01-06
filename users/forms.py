from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('phone_number','country', 'avatar_photo', 'email', 'password1', 'password2')