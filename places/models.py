from django.db import models

# Create your models here.
class Place(models.Model):
    Placename=models.CharField(max_length=200,primary_key=True)
    def save1(self):
        self.save()

    def __str__(self):
        return self.Placename


class Pn(models.Model):
    Placename1=models.CharField(max_length=200,primary_key=True)
    n0 = models.DecimalField(decimal_places=0,max_digits=5)
    n1 = models.DecimalField(decimal_places=0, max_digits=5)
    n2 = models.DecimalField(decimal_places=0, max_digits=5)
    n3 = models.DecimalField(decimal_places=0, max_digits=5)
    n4 = models.DecimalField(decimal_places=0, max_digits=5)

    def save2(self):
        self.save()

    def __str__(self):
        return self.Placename1



