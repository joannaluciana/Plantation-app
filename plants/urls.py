from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# stworzenie obiektu ruter
router.register('categories', views.CategoryViewSet, basename='category')
router.register('rooms', views.RoomViewSet, basename='room')
router.register('plants', views.PlantViewSet, basename='plant')
router.register('userplants', views.UserPlantViewSet, basename='userplant')
# router.register('account', views.AccountViewSet, basename='account') ciach jai 3jkczka
urlpatterns = [
    path('profile/', views.ProfileRetrieveView.as_view(), name='profile'),
    path('', include(router.urls)),
    ]
    # wchodzimy w api widok

    # router działa tylko z viewset - musi miec zaimplmntownae ListApdateCRUD