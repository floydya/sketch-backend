from cacheops import cached
from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    Group as NativeGroup,
)
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from phonenumber_field.modelfields import PhoneNumberField

from applications.accounts.manager import UserManager

__all__ = 'User', 'Group'


class Group(NativeGroup):
    class Meta:
        proxy = True
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class User(AbstractUser):
    GENDER_CHOICES = Choices(
        ('male', _("Male")),
        ('female', _("Female")),
    )
    username = None

    email = models.EmailField(
        unique=True, db_index=True,
    )

    first_name = models.CharField(
        _("First name"),
        max_length=144,
        blank=True,
    )

    middle_name = models.CharField(
        _("Middle name"),
        max_length=144,
        blank=True,
    )

    last_name = models.CharField(
        _("Last name"),
        max_length=144,
        blank=True,
    )

    gender = models.CharField(
        _("Gender"),
        choices=GENDER_CHOICES,
        max_length=32,
    )

    banned = models.BooleanField(
        _("Banned?"),
        default=False,
    )

    phone_number = PhoneNumberField(
        _("Phone number"),
        null=True,
        blank=True,
    )

    birth_date = models.DateField(
        _("Date of birth"),
        null=True,
        blank=True,
    )

    avatar = models.ImageField(
        _("Avatar"),
        upload_to='users/avatars',
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = tuple()
    FIELDS_TO_UPDATE = ('first_name', 'middle_name', 'last_name', 'phone_number', 'gender', 'birth_date', 'avatar')
    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

    @cached(timeout=10 * 60)
    def get_full_name(self):
        full_name = '%s %s %s' % (
            self.first_name, self.middle_name, self.last_name
        )
        return full_name.strip() or self.email

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
