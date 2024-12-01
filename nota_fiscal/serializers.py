from rest_framework import serializers
from .models import NotaFiscal

class nota_fiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = '_all_'