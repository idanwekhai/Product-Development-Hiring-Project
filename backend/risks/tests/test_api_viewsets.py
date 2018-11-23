import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from risk_types.models import RiskType

from ..models import Risk
from ..serializer import RiskSerializer

client = Client()


def get_valid_object():
    valid_object = {
        "risk_type": RiskType.objects.create(name="risk"),
        "name": "Test Name",
        "description": "Test Description"
    }
    return valid_object


def get_invalid_object():
    invalid_object = {
        "risk_type": "",
        "name": "",
        "description": ""
    }
    return invalid_object


class GetAllRisks(TestCase):
    """Test to GET every risk from API"""

    def setUp(self):
        Risk.objects.create(**get_valid_object())
        Risk.objects.create(**get_valid_object())

    def test_get_every_risks(self):

        response = client.get(reverse("risk-list"), format="json")

        # get data from database
        risks = Risk.objects.all()
        serializer = RiskSerializer(risks, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_every_risk_by_type(self):
        risk_type_id = 1

        response = client.get(reverse("risk-list-by-risk-type"),
                              {"risk_type_id": risk_type_id})

        # get data from database
        risks = Risk.objects.filter(risk_type_id=risk_type_id)
        serializer = RiskSerializer(risks, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleRisk(TestCase):
    """Test to GET single risk  from API"""

    def setUp(self):
        self.risk1 = Risk.objects.create(**get_valid_object())
        self.risk2 = Risk.objects.create(**get_valid_object())

    def test_get_valid_single_risk(self):

        response = client.get(reverse(
            "risk-detail",
            kwargs={"pk": self.risk1.pk}))

        # get data from database
        risk = Risk.objects.get(pk=self.risk1.pk)
        serializer = RiskSerializer(risk)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_risk(self):
        invalid_id = 450
        response = client.get(reverse(
            "risk-detail",
            kwargs={"pk": invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewRisk(TestCase):
    """Test for creaating a new risk"""

    def setUp(self):
        self.valid_risk = {
            "risk_type": RiskType.objects.create(name="risk").id,
            "name": "Test Name",
            "description": "Test Description"
        }
        self.invalid_risk = get_invalid_object()

    def test_create_valid_risk(self):

        response = client.post(reverse("risk-list"),
                               data=json.dumps(self.valid_risk),
                               content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_risk(self):

        response = client.post(reverse("risk-list"),
                               data=json.dumps(self.invalid_risk),
                               content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleRisk(TestCase):
    """Test to Update a single risk"""

    def setUp(self):
        self.risk = Risk.objects.create(**get_valid_object())

        self.valid_risk = {
            "risk_type": RiskType.objects.create(name="risk").id,
            "name": "Test Name",
            "description": "Test Description"
        }
        self.invalid_risk = get_invalid_object()

    def test_update_valid_risk(self):

        response = client.put(reverse(
            "risk-detail",
            kwargs={"pk": self.risk.pk}),
            data=json.dumps(self.valid_risk),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_single_risk(self):
        response = client.put(reverse(
            "risk-detail",
            kwargs={"pk": self.risk.pk}),
            data=json.dumps(self.invalid_risk),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleRisks(TestCase):
    """Test to DELETE single risk from API"""

    def setUp(self):
        self.risk = Risk.objects.create(**get_valid_object())

    def test_delete_valid_single_risk(self):

        response = client.delete(reverse(
            "risk-detail",
            kwargs={"pk": self.risk.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_risk(self):
        invalid_id = 450
        response = client.get(reverse(
            "risk-detail",
            kwargs={"pk": invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
