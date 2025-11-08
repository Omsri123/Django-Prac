from rest_framework import serializers
from .models import Blog, comments

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = '__all__'