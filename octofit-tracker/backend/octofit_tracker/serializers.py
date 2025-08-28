from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'team', 'is_superhero']


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'description']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    user = serializers.CharField(source='user.id', read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration', 'date']


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    team = serializers.CharField(source='team.name', read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']
