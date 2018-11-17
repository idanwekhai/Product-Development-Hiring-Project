from rest_framwork import viewsets

from .models import Risk
from .serializer import RiskSerializer


class RiskViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing Risks.
    """

    query_set = Risk.objects.all()
    serializer_class = RiskSerializer
