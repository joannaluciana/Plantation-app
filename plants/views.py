from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from .models import Category, Plant, Room, UserPlant
from .serializers import (
    AdminCategorySerializer,
    AdminPlantSerializer,
    AdminRoomSerializer,
    AdminUserPlantSerializer,
    CategorySerializer,
    RoomSerializer,
    PlantSerializer,
    UserPlantSerializer,
    UserSerializer,
)


class CategoryViewSet (viewsets.ModelViewSet):

    # ModelViewSet - obsługuje POST GET PATCH GET DELETE - nie musi ich
    # definiowac tak jak w viewsecie trzeba napisać te metody
    #
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminCategorySerializer
        return CategorySerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Category.objects.all()
            # dla admina chcemy zwrocic wszystkie kategorie
        return Category.objects.filter(user=self.request.user)

        # dla zalogonow ziomeczka - bedzie widzial tylko swoje kategorie
        # superuser widzi wszystko
    # nie trzeba szablonow


class RoomViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminRoomSerializer
        return RoomSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Room.objects.all()
        return Room.objects.filter(user=self.request.user)


class PlantViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminPlantSerializer
        return PlantSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Plant.objects.all()
        return Plant.objects.filter(user=self.request.user)


class UserPlantViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminUserPlantSerializer
        return UserPlantSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserPlant.objects.all()
        return UserPlant.objects.filter(user=self.request.user)


class ProfileRetrieveView(RetrieveAPIView):

    def retrieve(self, request, pk=None):
        User = get_user_model()
        serializer = UserSerializer(User.objects.get(pk=request.user.pk))
        return Response(serializer.data)

        # nie chcemy pobierać listy wszsytkich użytkownikow
