from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    CATEGORY_TYPES = (
        ('free', 'Free'),
        ('buy', 'Buy'),
    )
    
    category_name = models.CharField(max_length=100)
    category_type = models.CharField(max_length=100, choices=CATEGORY_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    points = models.IntegerField(default=30)
    slug = models.SlugField(max_length=100, unique=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    
    def __str__(self):
        return self.category_name


class Question(models.Model):
    question = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.question


class BuyCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mpin = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.category.category_name


class UserBoughtCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.category.category_name}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    daily_points = models.IntegerField(default=0)
    weekly_points = models.IntegerField(default=0)
    monthly_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ['-date_played']