from .models import *
from rest_framework.views import APIView
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.response import Response
from datetime import datetime, timezone
import calendar

class LeaderboardView(APIView):
    def get(self, request):
        now = datetime.now(timezone.utc)
        daily_reset_time = datetime(now.year, now.month, now.day, hour=23, minute=59, second=59, microsecond=0, tzinfo=timezone.utc)
        weekly_reset_time = datetime(now.year, now.month, now.day, hour=23, minute=59, second=59, microsecond=0, tzinfo=timezone.utc) + timedelta(days=(5-now.weekday()+7) % 7)
        last_day = calendar.monthrange(now.year, now.month)[1]
        monthly_reset_time = datetime(now.year, now.month, last_day, hour=23, minute=59, second=59, tzinfo=timezone.utc)
        
        if now >= daily_reset_time:
            Leaderboard.objects.all().update(daily_score=0)

        if now >= weekly_reset_time:
            Leaderboard.objects.all().update(weekly_score=0)

        if now >= monthly_reset_time:
            Leaderboard.objects.all().update(monthly_score=0)    
        
        daily_top = Leaderboard.objects.filter(user__is_active=True, user__is_staff=False,
            user__is_superuser=False)\
            .order_by('-daily_score')
        weekly_top = Leaderboard.objects.filter(user__is_active=True, user__is_staff=False,
            user__is_superuser=False)\
            .order_by('-weekly_score')
        monthly_top = Leaderboard.objects.filter(user__is_active=True, user__is_staff=False,
            user__is_superuser=False)\
            .order_by('-monthly_score')

        daily_scores = [profile.daily_points for profile in daily_top]
        weekly_scores = [profile.weekly_points for profile in weekly_top]
        monthly_scores = [profile.monthly_points for profile in monthly_top]
        daily_positions = [sorted(daily_scores, reverse=True).index(profile.daily_points) + 1 for profile in daily_top]
        weekly_positions = [sorted(weekly_scores, reverse=True).index(profile.weekly_points) + 1 for profile in weekly_top]
        monthly_positions = [sorted(monthly_scores, reverse=True).index(profile.monthly_points) + 1 for profile in monthly_top]

        data = {
            'daily': [{'username': profile.user, 'daily_score': profile.daily_points,'total_score': profile.points, 'position': daily_positions[i]}
                      for i, profile in enumerate(daily_top)],
            'weekly': [{'username': profile.user, 'weekly_score': profile.weekly_points,'total_score': profile.points, 'position':  weekly_positions[i] }
                       for i, profile in enumerate(weekly_top)],
            'monthly': [{'username': profile.user, 'monthly_score': profile.monthly_points,'total_score': profile.points, 'position':  monthly_positions[i] }
                       for i, profile in enumerate(monthly_top)],
        }
        return Response(data)