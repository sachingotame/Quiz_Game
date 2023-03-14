from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
import random

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
        
    def get_random_questions(slug):
        category = Category.objects.get(slug=slug)

        # Check if the category is free
        if category.category_type == 'free':
            questions = Question.objects.filter(slug=slug).order_by("?")[:5]
            # print(questions)
            serializer = QuestionSerializer(questions, many=True)
            context = {
                "data":serializer.data,
            }
            return Response(context)

