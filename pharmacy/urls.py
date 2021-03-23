from django.urls import path

from pharmacy import views

urlpatterns = [
    path("", views.PharmacyView.as_view(), name="add-get-pharmacy"),
    path("pharmacy-detail/<int:id>/", views.PharmacyDetailView.as_view(), name="pharmacy-detail"),
    path("pharmacy-address/", views.PharmacyAddressView.as_view(), name="pharmacy-address"),
]
