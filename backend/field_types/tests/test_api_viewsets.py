import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from ..models import FieldType
from ..serializer import FieldTypeSerializer

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


class GetAllFieldTypes(TestCase):
    """Test to GET every field type from API"""

    def setUp(self):
        FieldType.objects.create(**get_valid_object())
        FieldType.objects.create(**get_valid_object())

    def test_get_every_field_type(self):

        response = client.get(reverse("fieldtype-list"), format="json")

        # get data from database
        field_types = FieldType.objects.all()
        serializer = FieldTypeSerializer(field_types, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleFieldTypes(TestCase):
    """Test to GET single field type from API"""

    def setUp(self):
        self.field_type1 = FieldType.objects.create(**get_valid_object())
        self.field_type2 = FieldType.objects.create(**get_valid_object())

    def test_get_valid_single_field_type(self):

        response = client.get(reverse(
            "fieldtype-detail",
            kwargs={"pk": self.field_type1.pk}))

        # get data from database
        field_type = FieldType.objects.get(pk=self.field_type1.pk)
        serializer = FieldTypeSerializer(field_type)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_field_type(self):
        invalid_id = 450
        response = client.get(reverse(
            "fieldtype-detail",
            kwargs={"pk": invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewFieldTypes(TestCase):
    """Test for creaating a new field type"""

    def setUp(self):
        self.valid_field_type = get_valid_object()
        self.invalid_field_type = get_invalid_object()

    def test_create_valid_field_type(self):

        response = client.post(reverse("fieldtype-list"),
                               data=json.dumps(self.valid_field_type),
                               content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_field_type(self):

        response = client.post(reverse("fieldtype-list"),
                               data=json.dumps(self.invalid_field_type),
                               content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleFieldTypes(TestCase):
    """Test to Update a single field type"""

    def setUp(self):
        self.field_type = FieldType.objects.create(**get_valid_object())

        self.valid_field_type = get_valid_object()
        self.invalid_field_type = get_invalid_object()

    def test_update_valid_field_type(self):

        response = client.put(reverse(
            "fieldtype-detail",
            kwargs={"pk": self.field_type.pk}),
            data=json.dumps(self.valid_field_type),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_single_field_type(self):
        response = client.put(reverse(
            "fieldtype-detail",
            kwargs={"pk": self.field_type.pk}),
            data=json.dumps(self.invalid_field_type),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleFieldTypes(TestCase):
    """Test to DELETE single field type from API"""

    def setUp(self):
        self.field_type = FieldType.objects.create(**get_valid_object())

    def test_delete_valid_single_field_type(self):

        response = client.delete(reverse(
            "fieldtype-detail",
            kwargs={"pk": self.field_type.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_field_type(self):
        invalid_id = 450
        response = client.get(reverse(
            "fieldtype-detail",
            kwargs={"pk": invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
