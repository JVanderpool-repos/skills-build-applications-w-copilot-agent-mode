from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data using Djongo's MongoDB connection
        db = connection.cursor().db_conn
        db[Activity._meta.db_table].delete_many({})
        db[Leaderboard._meta.db_table].delete_many({})
        db[Workout._meta.db_table].delete_many({})
        db[User._meta.db_table].delete_many({})
        db[Team._meta.db_table].delete_many({})

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team='marvel', is_superhero=True),
            User(email='steve@rogers.com', name='Steve Rogers', team='marvel', is_superhero=True),
            User(email='bruce@wayne.com', name='Bruce Wayne', team='dc', is_superhero=True),
            User(email='clark@kent.com', name='Clark Kent', team='dc', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='cycle', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='yoga', duration=20, date=timezone.now().date())

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Upper body', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Core', suggested_for='dc')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
