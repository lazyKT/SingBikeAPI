"""
: API Endpoint URLs
"""
from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path ('users/', views.UserList.as_view()),
    path ('user/<str:user_id>', views.UserDetail.as_view()),
    path ('bikes/', views.BikeList.as_view()),
    path ('bike/<str:bike_id>', views.BikeDetail.as_view()),
    path ('trips/', views.TripList.as_view()),
]

urlpatterns = format_suffix_patterns (urlpatterns)
