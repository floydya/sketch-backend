from applications.transactions.models import Transaction
from shared.models import TransactionFilterSet as NativeTransactionFilterSet


class TransactionFilterSet(NativeTransactionFilterSet):
    class Meta:
        model = Transaction
        fields = (
            'created_at',
            'transaction_type',
            'purpose_id',
            'entity_type_id',
            'entity_id',
        )
