from rest_framework import viewsets

from .models import Risk
from .serializer import RiskSerializer


class RiskViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing Risks.
    """

    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
