from django.urls import path

from orders import views

urlpatterns = [
    path("", views.OrderView.as_view(), name="order"),
    path("order-detail/<int:id>/", views.OrderDetailView.as_view(), name="order-detail"),
]
