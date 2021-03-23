from django.urls import path

from drugs import views

urlpatterns = [
    path("", views.DrugsView.as_view(), name="add-get-drugs"),
    path("drugs-detail/<int:id>/", views.DrugsDetailView.as_view(), name="drugs-detail"),
]
