from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Patient

User = get_user_model()

# Custom Token Serializer to Include Role in Response
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role  # Add role to token payload
        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "role"]

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ["id", "username", "email", "role", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            role=validated_data["role"],
            password=validated_data["password"]  # Hashing handled automatically
        )
        return user

class PatientSerializer(serializers.ModelSerializer):
    receptionist = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Patient
        fields = "__all__"   