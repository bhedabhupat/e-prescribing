from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from drugs import serializers
from drugs.models import Drugs


# Create your views here.
class DrugsView(CreateAPIView, ListAPIView):
    serializer_class = serializers.DrugsSerializer
    queryset = Drugs.objects.all()
    permission_classes = (AllowAny,)
    __doc__ = "API to Add Drugs Details"


class DrugsDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = serializers.DrugsSerializer
    queryset = Drugs.objects.all()
    permission_classes = (AllowAny,)
    __doc__ = "API to GET, Update & Delete drugs detail"

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj
