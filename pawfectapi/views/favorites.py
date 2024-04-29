from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseServerError
from pawfectapi.views.sizes import SizeSerializer
from pawfectapi.views.play_styles import PlayStyleSerializer
from pawfectapi.models import Pet, Play_style, Size, Favorite
from pawfectapi.views.pets import UserSerializer
from django.contrib.auth.models import User


class PetSerializer(serializers.ModelSerializer):
    """JSON serializer for products"""

    play_style = PlayStyleSerializer()
    size = SizeSerializer()
    user = UserSerializer()

    class Meta:
        model = Pet
        fields = (
            "id",
            "user",
            "name",
            "breed",
            "size",
            "play_style",
            "bio",
        )


class FavoriteSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    pet = PetSerializer()

    class Meta:
        model = Favorite
        fields = (
            "id",
            "user",
            "pet",
        )
        depth = 1


class Favorites(ViewSet):
    """Request handlers for Favorites in Pawfect Platform"""

    def create(self, request):
        """Post request to add a favorite to the database
        {"pet_id": 8}
        """

        favorite = Favorite()
        favorite.user = request.auth.user
        chosen_pet_id = request.data["pet_id"]
        chosen_pet = Pet.objects.get(pk=chosen_pet_id)
        favorite.pet = chosen_pet
        favorite.save()

        serialized = FavoriteSerializer(favorite, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)
