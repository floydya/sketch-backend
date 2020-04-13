from django.contrib import admin

from jet.filters import RelatedFieldListFilter

from applications.transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_filter = 'purpose', 'transaction_type', ('entity_type', RelatedFieldListFilter),
    search_fields = 'transaction_code',

    def get_model_perms(self, request):
        return {}
