from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, pagination

from applications.transactions.api.filtersets import TransactionFilterSet
from applications.transactions.models import Transaction
from applications.transactions.api.serializers import TransactionSerializer


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    filter_backends = (DjangoFilterBackend,)
    filterset_class = TransactionFilterSet

    pagination_class = pagination.LimitOffsetPagination
