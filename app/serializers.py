from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Commentaire, Image, Lieu, RepCommentaire, Utilisateur,Caracteristique
class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'is_staff','last_name','first_name','email','is_active','is_staff']
class UtilisateurSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Utilisateur
        fields = "__all__"
class LieuxSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Lieu
        fields = "__all__"
class ImageSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Image
        fields = "__all__"
class ImageSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Image
        fields = "__all__"
class CaracteristiqueSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Caracteristique
        fields = "__all__"
class CommentaireSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Commentaire
        fields = "__all__"
class RepCommentaireSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = RepCommentaire
        fields = "__all__"

