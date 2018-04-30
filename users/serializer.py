from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

# from .models import Account, AccountManager
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(validated_data['username'][0], validated_data['email'][0], validated_data['password'][0])
