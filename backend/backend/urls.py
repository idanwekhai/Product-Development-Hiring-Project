from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from risks import views as risk_views
from fields import views as field_views
from risk_types import views as risk_type_views
from field_types import views as field_type_views
from fields_by_risk import views as fields_by_risk_views

router = routers.DefaultRouter()
router.register("risks", risk_views.RiskViewSet)
router.register("fields", field_views.FieldViewSet)
router.register("risk-types", risk_type_views.RiskTypeViewSet)
router.register("field-types", field_type_views.FieldTypeViewSet)
router.register("fields_by_risk", fields_by_risk_views.FieldByRiskViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
