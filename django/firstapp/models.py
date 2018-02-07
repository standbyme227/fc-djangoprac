from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
    ) #Choice는 각 튜플로 만들어서 데이터베이스에 저장될 값과 나타날 값을 분리시킨다.

    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    shirt_sizes = models.CharField(max_length=40, choices=SHIRT_SIZES)


class Musician(models.Model):
    first_name = models.CharField(max_length=30) # verbose name은 'first name'이 된다.
    # verbose name을 'musician's first name'으로 바꾸고 싶다면
    # first_name = models.CharField('musician's first name', max_length=30) 으로 하면된다.
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=40, blank=True, null=True)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name ="Musician's artist")
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Fruit(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

