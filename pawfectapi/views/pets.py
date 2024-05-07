from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.http import HttpResponseServerError
from pawfectapi.models import Pet, Play_style, Size, Favorite
from pawfectapi.views.play_styles import PlayStyleSerializer
from pawfectapi.views.sizes import SizeSerializer
from pawfectapi.views.users import UserSerializer
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
        depth = 1


class Pets(ViewSet):
    """Request handlers for Pets in Pawfect Platform"""

    def list(self, request):
        """Get list of all pets"""

        pets = Pet.objects.all()

        serializer = PetSerializer(pets, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Get one pet"""

        try:
            pet = Pet.objects.get(pk=pk)
            serializer = PetSerializer(pet, context={"request": request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Put request for a single pet
         {
        "name": "Chip",
        "breed": "Beagle mix",
        "size_id": 2,
        "play_style_id": 1,
        "bio": "Chip loves eating chips and watching trash reality television."
        }
        """

        pet = Pet.objects.get(pk=pk)

        # I don't think I need this??
        # user = User.objects.get(user=request.auth.user)
        # pet.user = user

        pet.name = request.data["name"]
        pet.breed = request.data["breed"]
        pet_size_id = request.data["size_id"]
        pet_size = Size(pk=pet_size_id)
        pet.size = pet_size
        pet_play_style_id = request.data["play_style_id"]
        pet_play_style = Play_style(pk=pet_play_style_id)
        pet.play_style = pet_play_style
        pet.bio = request.data["bio"]
        pet.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Post request to add a pet to the database
        {
        "name": "Chip",
        "breed": "Beagle mix",
        "size_id": 2,
        "play_style_id": 1,
        "bio": "Chip loves eating chips and watching trash reality television."
        }
        """
        pet = Pet()

        chosen_size_id = request.data["size_id"]
        pet_size = Size(pk=chosen_size_id)
        chosen_play_style_id = request.data["play_style_id"]
        pet_play_style = Play_style(pk=chosen_play_style_id)

        pet.user = request.auth.user
        pet.name = request.data["name"]
        pet.breed = request.data["breed"]
        pet.size = pet_size
        pet.play_style = pet_play_style
        pet.bio = request.data["bio"]
        pet.save()

        serialized = PetSerializer(pet, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        try:
            pet = Pet.objects.get(pk=pk)
            pet.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Pet.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response(
                {"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(methods=["get"], detail=False)
    def favorites(self, request):
        """Get all pets favorited by the current user"""

        user = request.auth.user
        favorited_pets = Favorite.objects.filter(user=user).values_list(
            "pet", flat=True
        )
        pets = Pet.objects.filter(id__in=favorited_pets)

        serializer = PetSerializer(pets, many=True, context={"request": request})

        return Response(serializer.data)

    @action(methods=["get"], detail=False)
    def user_pets(self, request):
        """Get all the user's pet profiles"""

        user = request.auth.user
        user_pet_profiles = Pet.objects.filter(user=user)

        serializer = PetSerializer(
            user_pet_profiles, many=True, context={"request": request}
        )

        return Response(serializer.data)
