from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = 'ContestCategory',


class ContestCategory(models.Model):

    name = models.CharField(
        _("Name"),
        max_length=144,
    )

    image = models.ImageField(
        upload_to='contest_categories',
    )

    class Meta:
        verbose_name = _("contest category")
        verbose_name_plural = _("contest categories")
