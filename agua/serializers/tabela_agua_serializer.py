from rest_framework import serializers

from ..models import TabelaAgua


class TabelaAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabelaAgua
        fields = '__all__'
