from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.core.mail import send_mail
from django.conf import settings

from .forms import UserRegisterForm
from .models import User


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Привет, спасибо за регистрацию'
        message = 'Нам очень приятно видеть Вас в нашей дружной семье!'
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [user_email])


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/detail.html'
    context_object_name = 'post'