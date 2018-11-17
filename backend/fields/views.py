from rest_framwork import viewsets

from .models import Field
from .serializer import FieldSerializer


class FieldViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing Fields.
    """

    query_set = Field.objects.all()
    serializer_class = FieldSerializer
