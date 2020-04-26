from django.shortcuts import render
from api.models import Category, Game
from api.serializers import CategorySerializer, GameSerializer
from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse

@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({"status":"505"}, safe=False)
    if request.method == 'POST':
        Category.objects.create(
            name = request.data['name']
        )
        return JsonResponse({'status':'200'}, safe=False)

@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        try:
            games = Game.objects.all()
            serializer = GameSerializer(games, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({"status":"505"}, safe=False)
    if request.method == 'POST':
        try:
            category = Category.objects.get(id=request.data['cat_id'])
        except:
            return JsonResponse({"status":"505"}, safe=False)
        Game.objects.create(
            category = category,
            name = request.data['name'],
            description = request.data['description'],
            image = request.data['image'],
            requirements = request.data['requirements']
        )
        return JsonResponse({"status": "200"}, safe=False)