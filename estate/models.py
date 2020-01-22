from django.db import models

# Create your models here.
class Post(models.Model):
    house_image = models.ImageField(upload_to = 'posts/')
    description = models.TextField(max_length=300)
    bedrooms_no = models.IntegerField()
    bathrooms_no = models.IntegerField()
    plot_size = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    