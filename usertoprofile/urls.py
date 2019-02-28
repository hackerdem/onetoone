from django.contrib import admin
from django.urls import path
from .views import CreateProfileView,DisplayDetailView

urlpatterns = [
    path('create', CreateProfileView.as_view(), name='create'),
    path('detail/<pk>', DisplayDetailView.as_view(),name='profile-detail')
]