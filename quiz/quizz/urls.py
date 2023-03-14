from django.urls import path
from quizz import leaderboard ,category ,question ,score 

urlpatterns = [

    #get/create all the category
    path('categories/', category.CategoryView.as_view(), name='category-list'),

    #for updating the exisiting category
    path('categories/<slug:slug>/', category.CategoryView.as_view(), name='quiz-category-update'),

    #get all the questions according to the category
    path('questions/<int:category_id>/', question.QuestionView.as_view(), name='quiz_questions'),

    #create questions
    path('questions/', question.QuestionView.as_view(),name='create new questions list'),

    #update the questions
    path('questions/<int:pk>/update/', question.QuestionView.as_view(), name='quiz-question-update'),

    #for posting result or answer
    path('quizr/<int:category_id>/', score.ScoreView.as_view(), name='quiz'),
    
    #for getting leadqerboard
     path('leaderboard/', leaderboard.LeaderboardView.as_view(), name='quiz-leaderboard'),
     
    ]
