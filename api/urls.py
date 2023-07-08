from django.urls import path
from .views import MisComprasAPIView


urlpatterns = [
    path('mis-compras/<int:pk>', MisComprasAPIView.as_view(), name='mis-compras'),
]
