from .models import UrlMapping
from rest_framework import serializers

class UrlMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrlMapping
        fields = ('id', 'original_url', 'short_code', 'created_at')
        read_only_fields = ("short_code","created_at")
