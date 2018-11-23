import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from ..models import RiskType
from ..serializer import RiskTypeSerializer

client = Client()


def get_valid_object():
    valid_object = {
        "name": "Test Name",
        "description": "Test Description"
    }
    return valid_object


def get_invalid_object():
    invalid_object = {
        "name": "",
        "description": ""
    }
    return invalid_object


class GetAllRiskTypes(TestCase):
    """Test to GET every risk type from API"""

    def setUp(self):
        RiskType.objects.create(**get_valid_object())
        RiskType.objects.create(**get_valid_object())

    def test_get_every_risk_type(self):

        response = client.get(reverse("risktype-list"), format="json")

        # get data from database
        risk_types = RiskType.objects.all()
        serializer = RiskTypeSerializer(risk_types, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleRiskTypes(TestCase):
    """Test to GET single risk type from API"""

    def setUp(self):
        self.risk_type1 = RiskType.objects.create(**get_valid_object())
        self.risk_type2 = RiskType.objects.create(**get_valid_object())

    def test_get_valid_single_risk_type(self):

        response = client.get(reverse(
            "risktype-detail",
            kwargs={"pk": self.risk_type1.pk}))

        # get data from database
        risk_type = RiskType.objects.get(pk=self.risk_type1.pk)
        serializer = RiskTypeSerializer(risk_type)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_risk_type(self):
        invalid_id = 450
        response = client.get(reverse(
            "risktype-detail",
            kwargs={"pk": invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewRiskTypes(TestCase):
    """Test for creaating a new risk type"""

    def setUp(self):
        self.valid_risk_type = get_valid_object()
        self.invalid_risk_type = get_invalid_object()

    def test_create_valid_risk_type(self):

        response = client.post(reverse("risktype-list"),
                               data=json.dumps(self.valid_risk_type),
                               content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_risk_type(self):

        response = client.post(reverse("risktype-list"),
                               data=json.dumps(self.invalid_risk_type),
                               content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleRiskTypes(TestCase):
    """Test to Update a single risk type"""

    def setUp(self):
        self.risk_type = RiskType.objects.create(**get_valid_object())

        self.valid_risk_type = get_valid_object()
        self.invalid_risk_type = get_invalid_object()

    def test_update_valid_risk_type(self):

        response = client.put(reverse(
            "risktype-detail",
            kwargs={"pk": self.risk_type.pk}),
            data=json.dumps(self.valid_risk_type),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_single_risk_type(self):
        response = client.put(reverse(
            "risktype-detail",
            kwargs={"pk": self.risk_type.pk}),
            data=json.dumps(self.invalid_risk_type),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleRiskTypes(TestCase):
    """Test to DELETE single risk type from API"""

    def setUp(self):
        self.risk_type = RiskType.objects.create(**get_valid_object())

    def test_delete_valid_single_risk_type(self):

        response = client.delete(reverse(
            "risktype-detail",
            kwargs={"pk": self.risk_type.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_risk_type(self):
        invalid_id = 450
        response = client.get(reverse(
            "risktype-detail",
            kwargs={"pk": invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
