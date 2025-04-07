from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    duration_minutes = models.IntegerField()  
    language = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title}--{self.director}--{self.release_date}--{self.genre}--{self.rating}--{self.duration_minutes}--{self.language}'






        return f'{self.name}'

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    genre = models.ManyToManyField(Genre,related_name='connection')
    def __str__(self):
        return f'{self.title}--{self.author}-{self.price}'
    
    
class Buyer(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    item = models.CharField(max_length=20)
    price = models.IntegerField()
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.item}-{self.price}'
    

