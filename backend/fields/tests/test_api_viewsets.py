import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from field_types.models import FieldType

from ..models import Field
from ..serializer import FieldSerializer

client = Client()

def get_valid_object():
    valid_object = {
        "field_type": FieldType.objects.create(name="field"),
        "label": "Test Label",
        "description": "Test Description"
    }
    return valid_object

def get_invalid_object():
    invalid_object = {
        "field_type": "",
        "label":"",
        "description":""
    }
    return invalid_object

class GetAllFields(TestCase):
    """Test to GET every field from API"""

    def setUp(self):
        Field.objects.create(**get_valid_object())
        Field.objects.create(**get_valid_object())

    def test_get_every_fields(self):

        response = client.get(reverse("field-list"), format="json")

        # get data from database
        fields = Field.objects.all()
        serializer = FieldSerializer(fields, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleField(TestCase):
    """Test to GET single field  from API"""

    def setUp(self):
        self.field1 = Field.objects.create(**get_valid_object())
        self.field2 = Field.objects.create(**get_valid_object())

    def test_get_valid_single_field(self):

        response = client.get(reverse(
            "field-detail", 
            kwargs={"pk": self.field1.pk}))

        # get data from database
        field = Field.objects.get(pk=self.field1.pk)
        serializer = FieldSerializer(field)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_field(self):
        invalid_id = 450
        response = client.get(reverse(
            "field-detail", 
            kwargs={"pk": invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewField(TestCase):
    """Test for creaating a new field"""

    def setUp(self):
        self.valid_field = {
        "field_type": FieldType.objects.create(name="field").id,
        "label": "Test Label",
        "description": "Test Description"
        }
        self.invalid_field = get_invalid_object()

    def test_create_valid_field(self):

        response = client.post(reverse("field-list"),
            data=json.dumps(self.valid_field),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_field(self):

        response = client.post(reverse("field-list"),
            data=json.dumps(self.invalid_field),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleField(TestCase):
    """Test to Update a single field"""

    def setUp(self):
        self.field = Field.objects.create(**get_valid_object())

        self.valid_field = {
        "field_type": FieldType.objects.create(name="field").id,
        "label": "Test Label",
        "description": "Test Description"
        }
        self.invalid_field = get_invalid_object()

    def test_update_valid_field(self):

        response = client.put(reverse(
            "field-detail", 
            kwargs={"pk": self.field.pk}),
            data=json.dumps(self.valid_field),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_single_field(self):
        response = client.put(reverse(
            "field-detail", 
            kwargs={"pk": self.field.pk}),
            data=json.dumps(self.invalid_field),
            content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleFields(TestCase):
    """Test to DELETE single field from API"""

    def setUp(self):
        self.field = Field.objects.create(**get_valid_object())

    def test_delete_valid_single_field(self):

        response = client.delete(reverse(
            "field-detail", 
            kwargs={"pk": self.field.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_field(self):
        invalid_id = 450
        response = client.get(reverse(
            "field-detail", 
            kwargs={"pk": invalid_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)