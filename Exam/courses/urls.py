from django.urls import path

from . import views

app_name="courses"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/rate/", views.RateView.as_view(), name="rate"),
    path("<int:course_id>/rate/submit", views.vote, name="vote"),
]
