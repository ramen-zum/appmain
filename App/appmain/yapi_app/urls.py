from rest_framework import routers
from .api import OrderViewSet, CompanyViewSet

router = routers.DefaultRouter()
router.register('api/order', OrderViewSet, 'orders')
router.register('api/companies', CompanyViewSet, 'companies')
urlpatterns = router.urls

