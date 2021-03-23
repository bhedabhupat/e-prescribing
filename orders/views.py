from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from orders import serializers
from orders.models import Booking
from user_profile.models import Medicines


class OrderView(CreateAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = Booking.objects.all()
    permission_classes = (IsAuthenticated,)
    __doc__ = "API to Place orders"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        instance = serializer.instance
        medicines = Medicines.objects.filter(prescription=instance.user_prescription)
        amount = sum([medicine.quantity * medicine.drugs.price for medicine in medicines])
        instance.amount = amount
        instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetailView(RetrieveAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = Booking.objects.all()
    permission_classes = (IsAuthenticated,)

    __doc__ = "API to get places orders"

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj
