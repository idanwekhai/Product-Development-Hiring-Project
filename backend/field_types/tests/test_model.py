from django.test import TestCase
from ..models import FieldType


class FieldTypeTestCase(TestCase):
    """Test cases for the FieldType Model"""

    def setUp(self):
        FieldType.objects.create(name="example field type name")

    def test_field_types_has_a_name(self):
        """test that field type has a name"""

        example_field_type = FieldType.objects.get(name="example field type name")

        self.assertTrue(example_field_type.name == "example field type name")

    def test_field_type_name(self):
        """test that a field type has the same name inserted"""

        field_type = FieldType.objects.get(name="example field type name")

        self.assertEqual(field_type.name, "example field type name")
