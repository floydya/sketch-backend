from drf_base64.fields import Base64ImageField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from applications.accounts.models import User


class UsernameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'id', 'email', 'get_full_name',


class UserSerializer(serializers.ModelSerializer):
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


class UserPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    repeat_new_password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        repeat_new_password = attrs.get('repeat_new_password')

        if new_password != repeat_new_password:
            raise serializers.ValidationError({
                'new_password': "Пароли должны совпадать!",
                'repeat_new_password': "Пароли должны совпадать!",
            })

        if old_password == new_password:
            raise serializers.ValidationError("Новый и старый пароли не отличаются!")

        if not self.instance.check_password(old_password):
            raise serializers.ValidationError({
                'old_password': "Текущий пароль введен неверно!",
            })

        return attrs

    def update(self, instance: User, validated_data):
        instance.set_password(validated_data.get('new_password'))
        instance.save()
        return instance

    def create(self, validated_data):
        pass


