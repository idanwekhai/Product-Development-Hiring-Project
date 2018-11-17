from rest_framework import viewsets

from .models import RiskType
from .serializer import RiskTypeSerializer


class RiskTypeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing RiskTypes.
    """

    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
