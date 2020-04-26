from drf_base64.fields import Base64ImageField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from applications.accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'id', 'email', 'get_full_name', 'avatar', 'phone_number'


class CurrentUserSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(
        required=False,
        allow_null=True
    )
    phone_number = PhoneNumberField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'full_name',
            'is_active',
            'is_staff',
            'is_superuser',
            'banned',
            'phone_number',
            'birth_date',
            'avatar',
            'date_joined',
            'last_login',
            'gender',
            'new_password',
            'confirm_new_password',
        )
        read_only_fields = (
            'id',
            'is_active',
            'is_staff',
            'is_superuser',
            'banned',
            'date_joined',
            'last_login',
        )

    def validate(self, attrs):
        new_password = attrs.get('new_password', None)
        confirm_new_password = attrs.get('confirm_new_password', None)

        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise serializers.ValidationError({
                "new_password": "Введенные пароли не совпадают!",
                "confirm_new_password": "Введенные пароли не совпадают!",
            })
        return attrs

    def create(self, validated_data):
        password, _p = validated_data.pop('new_password'), validated_data.pop('confirm_new_password')
        validated_data['password'] = password
        return User.objects.create_user(**validated_data)
