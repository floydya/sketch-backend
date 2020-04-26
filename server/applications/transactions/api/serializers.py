from rest_framework import serializers

from applications.accounts.api.serializers import UserSerializer
from applications.transactions.models import Transaction


class TransactionEntityRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        class AbstractSerializer(serializers.ModelSerializer):
            class Meta:
                model = value.__class__
                fields = '__all__'

        return AbstractSerializer(value).data


class TransactionSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    transaction_type = serializers.CharField(source='get_transaction_type_display')
    entity_type = serializers.CharField(source='entity_type.name')
    entity__type = serializers.CharField(source='entity_type.model')
    entity_object = TransactionEntityRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = (
            'id',
            'created_by',
            'created_at',
            'transaction_code',
            'transaction_type',
            'amount',
            'entity_type',
            'entity__type',
            'entity_id',
            'reference',
            'entity_object'
        )
        read_only_fields = fields
