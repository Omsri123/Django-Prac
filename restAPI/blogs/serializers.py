from rest_framework import serializers
from .models import Blog, comments

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = '__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many = True,read_only = True)
    class Meta:
        model = Blog
        fields = '__all__'

