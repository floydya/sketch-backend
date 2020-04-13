from rest_framework import viewsets, filters, generics, permissions

from applications.accounts.models import User
from applications.accounts.api.serializers import UserSerializer, UserPasswordSerializer
from shared.permissions import IsMeOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    permission_classes = IsMeOrReadOnly,

    filter_backends = filters.SearchFilter,
    search_fields = 'last_name', 'phone_number',


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = permissions.IsAuthenticated,

    def get_object(self):
        return self.request.user


class UserPasswordUpdateView(generics.UpdateAPIView):
    serializer_class = UserPasswordSerializer
    permission_classes = permissions.IsAuthenticated,

    def get_object(self):
        return self.request.user
