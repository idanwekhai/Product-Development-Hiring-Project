from django.test import TestCase
from ..models import RiskType


class RiskTypeTestCase(TestCase):
    """Test cases for the RiskType Model"""

    def setUp(self):
        RiskType.objects.create(name="example risk type name")

    def test_risk_types_has_a_name(self):
        """test that risk type has a name"""

        example_risk_type = RiskType.objects.get(name="example risk type name")

        self.assertTrue(example_risk_type.name == "example risk type name")

    def test_risk_type_name(self):
        """test that a risk type has the same name inserted"""

        risk_type = RiskType.objects.get(name="example risk type name")

        self.assertEqual(risk_type.name, "example risk type name")
