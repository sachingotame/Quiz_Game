from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.utils import timezone

class ScoreView(APIView):
    def post(self, request, category_id):
    # Check if the category exists
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)
        
        # Get the authenticated user
        user = request.user

        # Check if the user exists in the database
        if not user.id:
            return Response({'error': 'User not found'}, status=404)
        
        # Calculate the user's score
        score = 0
        results = []
        for answer in request.data:
            try:
                question = Question.objects.get(id=answer['question_id'], category_id=category_id)
            except Question.DoesNotExist:
                continue
            
            correct = question.correct_answer == answer['answer']
            score += category.points / 5 if correct else 0
            # print(score1)
            results.append({
                'id': question.id,
                'question': question.question,
                'correct': correct
            })

        # Update the leaderboard
        try:
            leaderboard = Leaderboard.objects.get(user_id=user, category_id=category)
            leaderboard.points += score
            leaderboard.daily_points += score
            leaderboard.weekly_points += score
            leaderboard.monthly_points += score


        except Leaderboard.DoesNotExist:
            leaderboard = Leaderboard(user_id=user, category_id=category, points=score, daily_points=score, weekly_points=score, monthly_points=score)
        leaderboard.save()
        
        return Response({'score': score, 'results': results})