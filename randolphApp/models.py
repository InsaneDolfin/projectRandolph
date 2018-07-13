from django.db import models

class Jeux(models.Model):
    name = models.CharField(max_length=200)
    section = models.CharField(max_length=50)
    note = models.CharField(max_length=500)
    disponibilite = models.CharField(max_length=50)
    etage = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Genre(models.Model):
    jeu = models.ForeignKey(Jeux, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)
    def __str__(self):
        return self.name
