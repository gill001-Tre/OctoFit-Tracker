from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel.name),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc.name),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Upper body', difficulty='easy'),
            Workout.objects.create(name='Running', description='Cardio', difficulty='medium'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=users[1], type='pushup', duration=15, date=timezone.now())
        Activity.objects.create(user=users[2], type='run', duration=45, date=timezone.now())
        Activity.objects.create(user=users[3], type='pushup', duration=20, date=timezone.now())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=110)
        Leaderboard.objects.create(user=users[3], score=95)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
