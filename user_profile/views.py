from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user_profile import serializers
from user_profile.models import *


class LoginAPIView(APIView):
    __doc__ = """Get user token by verifying username and password"""

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email__icontains=request.data.get("email")).first()
        if not (user and user.check_password(request.data.get("password"))):
            return Response({"status": False, "message": "Invalid User Detail"})
        if user:
            token, created = Token.objects.get_or_create(user=user)
            user.last_login = timezone.now()
            user.save()
            return Response({"status": True, "token": token.key})
        else:
            return Response({"status": False, "message": "Invalid user"})


class RegisterAPIView(CreateAPIView, ListAPIView):
    serializer_class = serializers.RegisterSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    __doc__ = "Registration API for user and get user list"

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, )


class UserDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = serializers.RegisterSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    __doc__ = "GET, Update and Delete user records "

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj


class PrescriptionView(CreateAPIView, UpdateAPIView):
    serializer_class = serializers.PrescriptionSerializer
    queryset = Prescription.objects.all()
    permission_classes = (IsAuthenticated,)

    __doc__ = "Prescription API to generate user and update user prescription"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = [Medicines(prescription=serializer.instance, drugs_id=value.get('drugs'), quantity=value.get('quantity'))
                for value in self.request.data.get('medicines')]
        Medicines.objects.bulk_create(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PrescriptionDetailView(RetrieveAPIView):
    serializer_class = serializers.PrescriptionSerializer
    queryset = Prescription.objects.all()
    permission_classes = (IsAuthenticated,)

    __doc__ = "API to retrieve generate user prescription"

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj


class UserAddressView(CreateAPIView):
    serializer_class = serializers.UserAddressSerializer
    queryset = UserAddress.objects.all()
    permission_classes = (IsAuthenticated,)

    __doc__ = "API to Add multiple user address"

    def create(self, request, *args, **kwargs):
        request.data["user"] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
