from django.db.models import QuerySet
from django.utils import timezone

from applications.contests.choices import DETAIL_CHOICES

__all__ = 'ContestQuerySet',


class ContestQuerySet(QuerySet):

    def detailed(self, detail):
        assert detail in DETAIL_CHOICES, "Detail value error!"
        return self.filter(details=detail)

    def expired(self):
        current_date = timezone.now().date()
        return self.filter(due_date__lt=current_date)

    def active(self):
        current_date = timezone.now().date()
        return self.filter(due_date__gte=current_date)
