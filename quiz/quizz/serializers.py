from rest_framework import serializers
from .models import Category, Question, BuyCategory, UserBoughtCategory, Leaderboard


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_type', 'price', 'points', 'slug', 'start', 'end']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class BuyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyCategory
        fields = '__all__'


class UserBoughtCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBoughtCategory
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        models = Leaderboard
        fields = '__all__'
