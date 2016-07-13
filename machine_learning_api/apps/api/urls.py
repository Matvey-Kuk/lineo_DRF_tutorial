from django.conf.urls import url, include
from rest_framework import routers

from views import CatViewSet

router = routers.DefaultRouter()
router.register(r'cat', CatViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]