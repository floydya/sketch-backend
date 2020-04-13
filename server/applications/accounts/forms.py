from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

__all__ = 'RegisterForm',


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.',
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='Optional.',
    )
    middle_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='Optional.',
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='Optional.',
    )
    birth_date = forms.DateField(
        required=False,
        help_text='Optional.',
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'password1',
            'password2',
            'gender',
            'birth_date',
        )
