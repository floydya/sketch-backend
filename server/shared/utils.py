import os

from django.utils import timezone


def get_upload_path(base_path):

    def _inner(instance, filename):
        return os.path.join(base_path, timezone.now().date().strftime("%Y/%m/%d"), filename)

    return _inner
