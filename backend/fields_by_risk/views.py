from rest_framework import viewsets

from .models import FieldByRisk
from .serializer import FieldByRiskSerializer


class FieldByRiskViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing FieldByRisk.
    """

    queryset = FieldByRisk.objects.all()
    serializer_class = FieldByRiskSerializer
