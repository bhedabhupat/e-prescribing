from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from pharmacy import serializers
from pharmacy.models import Pharmacy, PharmacyAddress


# Create your views here.
class PharmacyView(CreateAPIView, ListAPIView):
    serializer_class = serializers.PharmacySerializer
    queryset = Pharmacy.objects.all()
    permission_classes = (AllowAny,)

    __doc__ = "API to Add Pharmacy Details"


class PharmacyDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = serializers.PharmacySerializer
    queryset = Pharmacy.objects.all()
    permission_classes = (AllowAny,)

    __doc__ = "API to GET, Update & Delete pharmacy data"

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj


class PharmacyAddressView(generics.CreateAPIView):
    serializer_class = serializers.PharmacyAddressSerializer
    queryset = PharmacyAddress.objects.all()
    permission_classes = (IsAuthenticated,)

    __doc__ = "API to Add multiple Pharmacy address"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
