from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import TabelaAguaViewSet

router = DefaultRouter()
router.register(r'agua', TabelaAguaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
