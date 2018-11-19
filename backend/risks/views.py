from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route

from .models import Risk
from .serializer import RiskSerializer


class RiskViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing Risks.
    """

    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

    @list_route(url_path="list-by-risk-type")
    def list_by_risk_type(self, request):
        risk_type_id = self.request.query_params.get("risk_type_id", None)

        if risk_type_id is not None:
            risks = Risk.objects.filter(risk_type=risk_type_id)
            serializer = RiskSerializer(risks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_204_NO_CONTENT)
