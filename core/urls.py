from .views import FullThrottleAPI,PopulateDB
from django.urls import path

urlpatterns = [
    path('', FullThrottleAPI.as_view(),name="all"),
    path('PopulateDBApi', PopulateDB.as_view(), name="PopulateDB"),

]
