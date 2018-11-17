from rest_framwork import viewsets

from .models import FieldType
from .serializer import FieldTypeSerializer


class FieldTypeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing FieldTypes.
    """

    query_set = FieldType.objects.all()
    serializer_class = FieldTypeSerializer
