from rest_framework import viewsets
from .models import NotaFiscal
from .serializers import nota_fiscalSerializer

class NotaFiscalViewSet(viewsets.ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer_class = nota_fiscalSerializer