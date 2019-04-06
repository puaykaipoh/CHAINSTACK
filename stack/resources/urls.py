from django.urls import path
from .views import ResourceViewSet

urlpatterns = [
    path('', ResourceViewSet.as_view(), name='resource'),
]