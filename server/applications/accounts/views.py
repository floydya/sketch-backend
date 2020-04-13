from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (
    LoginView as NativeLoginView,
    PasswordResetView as NativePasswordResetView
)
from django.urls import reverse_lazy
from django.views.generic import CreateView

from applications.accounts.forms import RegisterForm
from applications.accounts.mixins import GuestRequired


class LoginView(GuestRequired, NativeLoginView):
    pass


class PasswordResetView(GuestRequired, NativePasswordResetView):
    pass


class RegisterView(GuestRequired, CreateView):
    success_url = reverse_lazy('index')
    form_class = RegisterForm
    template_name = "registration/registration_form.html"
    login_url = reverse_lazy('index')

    def test_func(self):
        return not self.request.user.is_authenticated

    def form_valid(self, form):
        user = authenticate(**{
            "email": form.cleaned_data.get('email'),
            "password": form.cleaned_data.get('password1')
        })
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)
