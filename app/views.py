from django.shortcuts import render
from urllib import request
from django.contrib.auth.models import User
from app.models import Caracteristique, Commentaire, Image, Lieu, RepCommentaire, Utilisateur
from app.myPagination import MyPagination
from app.serializers import CaracteristiqueSerializer, CommentaireSerializer, ImageSerializer, LieuxSerializer, RepCommentaireSerializer, UserSerializer, UtilisateurSerializer
from rest_framework import  viewsets,permissions
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user']
class LieuViewSet(viewsets.ModelViewSet):
    queryset = Lieu.objects.all()
    pagination_class=MyPagination
    serializer_class = LieuxSerializer
    filterset_fields = ['id', 'nom','secteur','departement','region','type']
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    ordering_fields = ('created_at','update_at')
class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    pagination_class=MyPagination
    serializer_class = CommentaireSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    ordering_fields = ('created_at','update_at')
    filterset_fields = ['id', 'commentaire','lieu']
class RepCommentaireViewSet(viewsets.ModelViewSet):
    queryset = RepCommentaire.objects.all()
    serializer_class = RepCommentaireSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    ordering_fields = ('created_at','update_at')
    filterset_fields = ['id', 'commentaire','reponse']
class CaracteristiqueViewSet(viewsets.ModelViewSet):
    queryset = Caracteristique.objects.all()
    serializer_class = CaracteristiqueSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    ordering_fields = ('created_at','update_at')
    filterset_fields = ['id', 'commentaire']
    ordering_fields = 'created_at'