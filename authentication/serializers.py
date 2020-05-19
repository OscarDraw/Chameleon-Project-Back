from rest_framework import serializers
from authentication.models import Login, UserStatus, UserInfo, Role


class CreateNewUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    password = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        exclude = ['password', 'created_at', 'updated_at', 'trashed', 'trashed_at']

class UserStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserStatus
        exclude = ['created_at', 'updated_at', 'trashed', 'trashed_at']

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        exclude = ['created_at', 'updated_at', 'trashed', 'trashed_at']


class UserInfoSerializer(serializers.ModelSerializer):
    login = LoginSerializer()
    status = UserStatusSerializer()
    role = RoleSerializer()

    class Meta:
        model = UserInfo
        exclude = ['created_at', 'updated_at', 'trashed', 'trashed_at']