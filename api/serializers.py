from rest_framework import serializers
from api.models import Category, Game

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name'

class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    category = CategorySerializer()
    name = serializers.CharField()
    description = serializers.CharField()
    image = serializers.CharField()
    requirements = serializers.CharField()
    