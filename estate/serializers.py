from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Picture


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True, 'required': True}}

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','house_image', 'description', 'location', 'bedrooms_no', 'bathrooms_no', 'plot_size', 'cost', 'pub_date')

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id','description', 'location', 'pub_date')
