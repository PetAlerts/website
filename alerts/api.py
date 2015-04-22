from rest_framework import serializers, viewsets
from .models import Alert


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert


class AlertList(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
