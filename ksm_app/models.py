from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Debatants(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null = True)

    imię = models.CharField(max_length = 256)
    nazwisko = models.CharField(max_length = 256)
    email = models.EmailField(max_length = 256, null = True)
    miasto = models.CharField(max_length = 256)
    szkoła = models.CharField(max_length = 256)
    organizacja = models.CharField(max_length = 256)
    facebook = models.URLField(max_length = 256, null = True)
    opis = models.TextField(max_length=1000, null = True)
    terminy = models.TextField(max_length=1000, null = True)

    class Meta:
        ordering = ['imię']

    def __str__(self):
        return (self.imię + ' ' + self.nazwisko)

class Judges(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE, null = True)

    imię = models.CharField(max_length = 256)
    nazwisko = models.CharField(max_length = 256)
    email = models.EmailField(max_length = 256, null = True)
    miasto = models.CharField(max_length = 256)
    szkoła = models.CharField(max_length = 256)
    organizacja = models.CharField(max_length = 256)
    dyspozycyjnosc = models.TextField(max_length= 1000)
    opis = models.TextField(max_length = 2000)
    facebook = models.URLField(max_length = 256, null = True)

    class Meta:
        ordering = ['imię']

    def __str__(self):
        return (self.imię + ' ' + self.nazwisko)

class DebatantsBattle(models.Model):
    user1 = models.ForeignKey(Debatants, related_name="user1", on_delete=models.SET_NULL, null = True)
    user2 = models.ForeignKey(Debatants, related_name="user2", on_delete=models.SET_NULL, null = True)
    judge = models.ForeignKey(Judges, on_delete=models.SET_NULL, null = True)
    data = models.DateField(max_length=256, null = True)
    godzina = models.TimeField(max_length = 256, null = True)
    transmisja = models.URLField(blank=True)


    def __str__(self):
        return (self.user1.nazwisko + ' vs ' +  self.user2.nazwisko)


class PasswordJudges(models.Model):
    haslo = models.CharField(max_length = 11)

    def __str__(self):
        return self.haslo
