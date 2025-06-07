from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    def validate(self, attrs):
        # Поддержка логина по email (без учета регистра)
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            email = email.lower()
            try:
                user = User.objects.get(email__iexact=email)
                attrs['username'] = user.username
                attrs['password'] = password  # Явно подставляем пароль
            except User.DoesNotExist:
                pass
        return super().validate(attrs)

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
    permission_classes = [AllowAny]