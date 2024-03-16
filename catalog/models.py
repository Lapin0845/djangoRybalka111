from django.db import models

# Create your models here.
class Rybalka(models.Model):
    opis = models.CharField(max_length=300)
    price = models.IntegerField()
    image = models.ImageField(max_length=300)
    skidka = models.FloatField(default=1)

class Ohota(models.Model):
    opis = models.CharField(max_length=300)
    price = models.IntegerField()
    image = models.ImageField(max_length=300)
    skidka = models.FloatField(default=1)

class Odejda(models.Model):
    opis = models.CharField(max_length=300)
    price = models.IntegerField()
    image = models.ImageField(max_length=300)
    skidka = models.FloatField(default=1)

class Korzina(models.Model):
    rybalka = models.ForeignKey(Rybalka, on_delete=models.CASCADE)
    count = models.IntegerField()
    summa = models.DecimalField(decimal_places=2, max_digits=8)

    def calcSumma(self):
        return self.count * self.rybalka.price

class Korzina_2(models.Model):
    ohota = models.ForeignKey(Ohota, on_delete=models.CASCADE)
    count = models.IntegerField()
    summa = models.DecimalField(decimal_places=2, max_digits=8)

    def calcSumma2(self):
        return self.count * self.ohota.price


class Korzina_3(models.Model):
    odejda = models.ForeignKey(Odejda, on_delete=models.CASCADE)
    count = models.IntegerField()
    summa = models.DecimalField(decimal_places=2, max_digits=8)

    def calcSumma3(self):
        return self.count * self.odejda.price