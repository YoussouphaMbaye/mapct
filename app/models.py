from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lieu(models.Model):
    nom=models.CharField(max_length=255,blank=True,null=True)
    region=models.CharField(max_length=255,blank=True,null=True)
    commune=models.CharField(max_length=255,blank=True,null=True)
    departement=models.CharField(max_length=255,blank=True,null=True)
    secteur=models.CharField(max_length=255,blank=True,null=True)
    type=models.CharField(max_length=255,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    latitude=models.CharField(max_length=255,blank=True,null=True)
    longitude=models.CharField(max_length=255,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)
    photos = models.FileField(upload_to='photos/')
    def __str__(self) -> str:
        return self.nom
class Image(models.Model):
    photos = models.FileField(upload_to='photos/')
    lieu=models.ForeignKey(Lieu,on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)
   
    def __str__(self) -> str:
        return self.lieu
class Caracteristique(models.Model):
    nom=models.CharField(max_length=255,blank=True,null=True)
    valeur=models.CharField(max_length=255,blank=True,null=True)
    lieu=models.ForeignKey(Lieu,on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)
   
    def __str__(self) -> str:
        return self.nom
class Commentaire(models.Model):
    commentaire=models.TextField(max_length=355,blank=True,null=True)
    email=models.CharField(max_length=255,blank=True,null=True)
    nom=models.CharField(max_length=255,blank=True,null=True)
    lieu=models.ForeignKey(Lieu,on_delete=models.CASCADE)
    # class Meta:
    #     unique_together = (('lieu', 'user'),)

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)
   
    def __str__(self) -> str:
        return self.commentaire
class RepCommentaire(models.Model):
    reponse=models.TextField(max_length=355,blank=True,null=True)
    email=models.CharField(max_length=255,blank=True,null=True)
    nom=models.CharField(max_length=255,blank=True,null=True)
    commentaire=models.ForeignKey(Commentaire,on_delete=models.CASCADE)
    
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)
   
    def __str__(self) -> str:
        return self.commentaire
    
class Utilisateur(models.Model):
    telephone=models.CharField(max_length=20,blank=True,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
   
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self) -> str:
        return self.telephone