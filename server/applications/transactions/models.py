from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _

from applications.accounts.models import User
from shared.models.transaction import AbstractTransaction

__all__ = 'Transaction',


class Transaction(AbstractTransaction):
    purpose_model = User

    purpose = models.ForeignKey(
        purpose_model,
        on_delete=models.PROTECT,
        related_name='transactions',
        verbose_name=_("Purpose")
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('transaction')
        verbose_name_plural = _('transactions')
        indexes = (
            BrinIndex(fields=('created_at',)),
        )
