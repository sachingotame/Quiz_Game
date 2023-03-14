# from django.shortcuts import get_object_or_404
# from django.views import View
# from rest_framework.response import Response
# from .models import Category, Question, Answer, Leaderboard

# class PlayView(View):
#     def post(self, request):
#         # Get the question id from the request
#         question_id = request.data.get('question_id')
        
#         # Get the category of the question
#         question = get_object_or_404(Question, id=question_id)
#         category = question.category
#         points = category.points
#         total_points = (points / 5) * 
        
#         # Update the leaderboard
#         leaderboard = get_object_or_404(Leaderboard, user=request.user)
#         leaderboard.points += total_points
#         leaderboard.daily_points += total_points
#         leaderboard.weekly_points += total_points
#         leaderboard.weekly_points += total_points
#         leaderboard.save()
        
#         return Response({'points': total_points})
