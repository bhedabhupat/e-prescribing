from django.urls import path
from rest_framework import routers

from user_profile import views

router = routers.DefaultRouter()

urlpatterns = [
    path("login/", views.LoginAPIView.as_view(), name="login", ),
    path("register/", views.RegisterAPIView.as_view(), name="register", ),
    path("user-list/", views.RegisterAPIView.as_view(), name="user-list"),
    path("user-detail/<int:id>/", views.UserDetailView.as_view(), name="user-detail"),
    path("user-prescription/", views.PrescriptionView.as_view(), name="user-prescription"),
    path("user-prescription-detail/<int:id>/", views.PrescriptionDetailView.as_view(), name="user-prescription-detail"),
    path("user-address/", views.UserAddressView.as_view(), name="user-address"),
]
