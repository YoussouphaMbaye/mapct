from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.urls import path,include
from .views import CaracteristiqueViewSet, ImageViewSet, RepCommentaireViewSet, UserViewSet, LieuViewSet,CommentaireViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('lieux', LieuViewSet)
router.register('cmmentaires', CommentaireViewSet)
router.register('reponses', RepCommentaireViewSet)
router.register('caracteristiques', CaracteristiqueViewSet)
router.register('images', ImageViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]