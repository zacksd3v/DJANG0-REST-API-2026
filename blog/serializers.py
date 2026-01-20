from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) # anan dole sunan 'comments' yyi iri 1 da na model.py a wurin da aka sanya related_name='comments'
    class Meta:
        model = Blog
        fields = '__all__'