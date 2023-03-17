from rest_framework.routers import DefaultRouter

from .views import ProductView

router = DefaultRouter()
router.register('product', ProductView)


urlpatterns = []
urlpatterns += router.urls