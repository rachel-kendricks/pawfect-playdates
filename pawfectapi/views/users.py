from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        )


class Users(ViewSet):
    """Request handlers for User in Pawfect Platform"""

    def retrieve(self, request, pk=None):
        """Get User info by ID"""

        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={"request": request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Put request to update profile/user info
        {
        "first_name": "Joe",
        "last_name": "Shepherd",
        "username": "joe2",
        "email": "newEmail@example.com",
        }
        """

        user = User.objects.get(pk=pk)

        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.username = request.data["username"]
        user.email = request.data["email"]
        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Delete a user from the database"""

        try:
            user = User.objects.get(pk=pk)
            user.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except User.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
