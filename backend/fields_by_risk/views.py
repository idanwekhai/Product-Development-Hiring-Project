from rest_framwork import viewsets

from .models import FieldByRisk
from .serializer import FieldByRiskSerializer


class FieldByRiskViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing FieldByRisk.
    """

    query_set = FieldByRisk.objects.all()
    serializer_class = FieldByRiskSerializer
