from django.urls import path
from rest_framework.routers import DefaultRouter

from vehicle.apps import VehicleConfig
from vehicle.views import CarViewSet, MotoCreateApiView, MotoListApiView, MotoRetrieveApiView, MotoUpdateApiView, \
    MotoDestroyApiView, MilageCreateApiView

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
                  path('moto/create/', MotoCreateApiView.as_view(), name='moto-create'),
                  path('moto/', MotoListApiView.as_view(), name='moto-list'),
                  path('moto/<int:pk>/', MotoRetrieveApiView.as_view(), name='moto-get'),
                  path('moto/update/<int:pk>/', MotoUpdateApiView.as_view(), name='moto-update'),
                  path('moto/delete/<int:pk>/', MotoDestroyApiView.as_view(), name='moto-delete'),

                  # milage
                  path('milage/create/', MilageCreateApiView.as_view(), name='Milage-create'),

              ] + router.urls
