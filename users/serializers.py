from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password',
                  'last_login', 'last_activity']
        extra_kwargs = {'email': {'required': True}}
