from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'autor', 'content', 'date_time', 'total_likes']
        read_only_fields = ['id', 'autor', 'date_time', 'total_likes']
    
    def get_total_likes(self, obj):
        return obj.likes.count()