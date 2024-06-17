from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

# Create your models here.

class Genre(models.Model):
    caption = models.CharField(max_length=20)

    def genre_name(self): 
        return f"{self.caption}"
    
    def __str__(self):
        return self.genre_name()

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="books")
    blurb = models.TextField(validators=[MinLengthValidator(10)])
    genre = models.ForeignKey(Genre , null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField( default=3, validators=[MaxValueValidator(10), MinValueValidator(1)])