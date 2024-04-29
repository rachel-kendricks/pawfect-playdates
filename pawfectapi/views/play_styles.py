from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from pawfectapi.models import Play_style


class PlayStyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Play_style
        fields = (
            "id",
            "name",
        )


class PlayStyles(ViewSet):
    """Request handlers for Play style in Pawfect Platform"""

    def list(self, request):
        """Get list of all play styles"""

        play_styles = Play_style.objects.all()

        serializer = PlayStyleSerializer(
            play_styles, many=True, context={"request": request}
        )
        return Response(serializer.data)
