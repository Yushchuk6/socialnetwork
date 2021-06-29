from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class RegisterViewSet(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class AccountViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "username"