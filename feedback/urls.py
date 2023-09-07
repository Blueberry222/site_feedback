from django.urls import path

from . import views

urlpatterns = [
    path("<int:feedback_id>/", views.detail, name="detail"),
    path("create_feedback/", views.create_feedback, name="create_feedback"),
    path("", views.index, name="index")
]