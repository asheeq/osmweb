from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from osmweb.users.api.views import UserViewSet
from osmweb.categories.views import CategoryViewSet, ProductViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)


app_name = "api"
urlpatterns = router.urls
