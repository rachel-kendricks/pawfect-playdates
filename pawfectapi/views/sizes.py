from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from pawfectapi.models import Size


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = (
            "id",
            "name",
        )


class Sizes(ViewSet):
    """Request handlers for Play style in Pawfect Platform"""

    def list(self, request):
        """Get list of all play styles"""

        sizes = Size.objects.all()

        serializer = SizeSerializer(sizes, many=True, context={"request": request})
        return Response(serializer.data)
