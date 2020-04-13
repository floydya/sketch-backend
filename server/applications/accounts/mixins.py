from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

__all__ = 'GuestRequired',


class GuestRequired(UserPassesTestMixin):
    redirect_to = None

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        if self.redirect_to:
            return redirect(self.redirect_to)
        return redirect('index')
