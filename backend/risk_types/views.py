from rest_framwork import viewsets

from .models import RiskType
from .serializer import RiskTypeSerializer


class RiskTypeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing RiskTypes.
    """

    query_set = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
