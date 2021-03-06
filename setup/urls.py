from django.contrib import admin
from django.urls import path, include
from api.views import PessoaViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('pessoa', PessoaViewSet, basename='Pessoas')
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(router.urls)),
]
