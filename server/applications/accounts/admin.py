from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as NativeUserAdmin,
    Group as NativeGroup,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from applications.accounts.models import User, Group
from shared.admin import RedirectMixin

admin.site.unregister(NativeGroup)
admin.site.register(Group)


@admin.register(User)
class UserAdmin(RedirectMixin, NativeUserAdmin):
    list_select_related = True
    list_filter = ['is_active', 'banned']
    readonly_fields = ('last_login', 'date_joined', 'get_transaction_redirect')
    search_fields = ('get_full_name',)
    ordering = ['id']
    fieldsets = [
        [None, {
            'fields': [
                'email', 'password',
                'first_name', 'middle_name', 'last_name',
                'phone_number', 'birth_date', 'avatar',
                'get_transaction_redirect'
            ]
        }],
        [_("Permissions"), {
            'fields': [
                'is_active',
                'banned',
                'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            ]
        }],
        [_("Dates"), {
            'fields': ['last_login', 'date_joined']
        }]
    ]
    list_display = (
        'id', 'get_full_name',
        'is_active', 'banned',
    )
    list_display_links = ('id',)
    add_fieldsets = (None, {
        'classes': ('wide',),
        'fields': (
            'email', 'password1', 'password2',
            'first_name', 'middle_name', 'last_name',
            'phone_number', 'birth_date', 'avatar',
        ),
    }),

    def get_transaction_redirect(self, instance):
        url = reverse('admin:transactions_transaction_changelist') + f'?purpose__id__exact={instance.id}'
        return self.redirect_url(url)

    get_transaction_redirect.short_description = _("Transactions")
