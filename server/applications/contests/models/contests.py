from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField

from applications.contests.choices import DETAIL_CHOICES
from applications.contests.managers import ContestQuerySet
from shared.utils import get_upload_path

__all__ = 'Contest', 'Example',


class Contest(models.Model):
    DETAIL_CHOICES = DETAIL_CHOICES

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name=_("Customer"),
    )
    created_at = models.DateTimeField(
        _("Created at"),
        default=timezone.now,
    )

    title = models.CharField(
        _("Title"),
        max_length=256,
        help_text=_("Enter the title for your custom tattoo design.")
    )

    description = models.TextField(
        _("Description"),
        help_text=_("""
        Describe your tattoo design. 
        Where will it be located? 
        What colors do you want? 
        Does your tattoo design include any text? 
        Please be as specific and detailed as possible.
        """)
    )

    due_date = models.DateField(
        _("Due date"),
    )

    category = models.ForeignKey(
        'contests.ContestCategory',
        on_delete=models.PROTECT,
        related_name='contests',
        verbose_name=_("Contest category"),
    )

    width = models.DecimalField(
        _("Width"),
        max_digits=12,
        decimal_places=2,
    )
    height = models.DecimalField(
        _("Height"),
        max_digits=12,
        decimal_places=2,
    )

    details = models.CharField(
        _("Details"),
        choices=DETAIL_CHOICES,
        max_length=1
    )

    price = MoneyField(
        _("Price"),
        max_digits=14,
        decimal_places=2,
        default_currency=settings.DEFAULT_CURRENCY,
    )

    billed_price = MoneyField(
        _("Billed price"),
        max_digits=14,
        decimal_places=2,
        default_currency=settings.DEFAULT_CURRENCY,
    )

    objects = ContestQuerySet.as_manager()

    class Meta:
        verbose_name = _("contest")
        verbose_name_plural = _("contests")


class Example(models.Model):
    contest = models.ForeignKey(
        Contest,
        on_delete=models.CASCADE,
        related_name='examples',
        verbose_name=_("Contest"),
    )

    image = models.ImageField(
        upload_to=get_upload_path('examples'),
    )

    class Meta:
        verbose_name = _("example image")
        verbose_name_plural = _("example images")
