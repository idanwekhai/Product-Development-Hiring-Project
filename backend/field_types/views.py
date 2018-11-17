from rest_framework import viewsets

from .models import FieldType
from .serializer import FieldTypeSerializer


class FieldTypeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing FieldTypes.
    """

    queryset = FieldType.objects.all()
    serializer_class = FieldTypeSerializer
