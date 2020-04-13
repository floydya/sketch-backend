from django.utils.translation import gettext_lazy as _

__all__ = 'DETAIL_CHOICES',


DETAIL_CHOICES = (
    ('l', _("Low detailed")),
    ('m', _("Medium detailed")),
    ('h', _("High detailed")),
    ('t', _("Text only")),
)
