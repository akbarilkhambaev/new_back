from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from django.contrib.auth.models import User

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            try:
                user = User.objects.get(email__iexact=email)
                attrs['username'] = user.username
            except User.DoesNotExist:
                raise serializers.ValidationError("No active account found with this email.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")
        return super().validate(attrs)

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
    permission_classes = [AllowAny]
