from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class QuestionView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response({'error': ' not found'}, status=404)
    
    def put(self, request, pk):
            quiz_question = self.get_object(pk)
            serializer = QuestionSerializer(quiz_question, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, category_id):

        category = Category.objects.get(id=category_id)

        # last_played = Leaderboard.objects.filter(user_id=user, category_id=category_id).first()
        # if not last_played and last_played.date_played >= timezone.now() - timezone.timedelta(days=1):
            # If user has already played this category's questions today, return an error response
            # return Response({"error": "You have already played this category's questions today. Please try again tomorrow."}, status=status.HTTP_403_FORBIDDEN)    
            # Check if the category is free

        if category.category_type == 'free':
            questions = Question.objects.filter(category_id=category_id).order_by("?")[:5]
            # print(questions)
            serializer = QuestionSerializer(questions, many=True)
            context = {
                "data":serializer.data,
            }
            return Response(context)

        elif category.category_type == 'buy':
            if UserBoughtCategory.objects.filter(user=request.user, category_id=category_id).exists():
                questions = Question.objects.filter(category_id=category_id)
                serializer = QuestionSerializer(questions, many=True)
                context = {    
                    "data":serializer.data,
                }
                return Response(context)
            else:
                return Response("Unbought category")