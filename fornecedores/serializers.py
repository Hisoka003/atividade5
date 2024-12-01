from rest_framework import serializers
from .models import Fornecedor

class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'