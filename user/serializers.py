from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from user.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token["token_message"] = "sparta_time_attack"

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user
