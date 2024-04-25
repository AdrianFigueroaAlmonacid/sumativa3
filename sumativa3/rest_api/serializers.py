from rest_framework import serializers
from core.models import series


class seriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = series
        fields = ['titulo', 'origen', 'chapters', 'estreno']
