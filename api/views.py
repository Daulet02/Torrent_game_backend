from django.shortcuts import render
from api.models import Category, Game, Comment
from api.serializers import CategorySerializer, GameSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse
from rest_framework.views import APIView
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

class CategoryView(APIView):
    def get_cat(self, id):
        try:
            category = Category.objects.get(id=id)
            return category
        except:
            return JsonResponse({"status":"505"}, safe=False)
    
    def get(self, request, id):
        category = self.get_cat(id)
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data, safe=False)
    def put(self, request, id):
        category = self.get_cat(id)
        category.name = request.data.get('name')
        category.save()
        return JsonResponse({'status':'200'}, safe=False)
    def delete(self, request, id):
        category = self.get_cat(id)        
        category.delete()
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
            category = Category.objects.get(name=request.data['category'])
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

class GameView(APIView):
    def get_game(self, id):
        try:
            game = Game.objects.get(id=id)
            return game
        except:
            return JsonResponse({"status":"505"}, safe=False)
    
    def get(self, request, id):
        game = self.get_game(id)
        serializer = GameSerializer(game)
        return JsonResponse(serializer.data, safe=False)

    def put(self,request,id):
        game = self.get_game(id)
        game.name = request.data.get('name')
        game.description = request.data.get('description')
        game.requirements = request.data.get('requirements')
        game.image = request.data.get('image')
        game.save()
        return JsonResponse({"status": "200"}, safe=False)

    def delete(self,request,id):
        game = self.get_game(id)
        game.delete()
        return JsonResponse({"status": "200"}, safe=False) 


class CommentView(APIView):
    def post(self, request):
        try:
            game = Game.objects.get(name=request.data.get('game'))
        except:
            return JsonResponse({"error": "cant get game(((("}, safe=False)
        Comment.objects.create(
            username = request.data.get('username'),
            text = request.data.get('text'),
            game = game
        )
        return JsonResponse({"status": "200"}, safe=False)

    def get(self, request):
        try:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({"status":"505"}, safe=False)