from django.db import models

# Create your models here.
class Post(models.Model):
    house_image = models.ImageField(upload_to = 'posts/')
    description = models.TextField(max_length=300)
    location = models.CharField(max_length=100)
    bedrooms_no = models.PositiveIntegerField()
    bathrooms_no = models.PositiveIntegerField()
    plot_size = models.PositiveIntegerField()
    cost = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)

class Picture(models.Model):
    description = models.TextField(max_length=300)
    location = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    