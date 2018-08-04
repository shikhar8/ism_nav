from django.db import models

# Create your models here.
class Place(models.Model):
    Placename=models.CharField(max_length=200)
    number=models.AutoField(primary_key=True)
    def save1(self):
        self.save()

    def __str__(self):
        return self.Placename


