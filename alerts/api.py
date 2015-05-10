from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Alert


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 20


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert


class AlertSerializerWithDisplay(AlertSerializer):
    gender = serializers.CharField(source='get_gender_display')
    species = serializers.CharField(source='get_species_display')
    age = serializers.CharField(source='get_age_display')


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        """
        The successful POST response should
        use `AlertSerializerWithDisplay`.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created = serializer.save()
        new_data = AlertSerializerWithDisplay(created).data
        new_data['picture'] = request.build_absolute_uri(new_data['picture'])
        headers = self.get_success_headers(new_data)
        return Response(new_data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AlertSerializerWithDisplay
        return AlertSerializer
