from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Match(models.Model):
    date = models.DateField()
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)

class Prediction(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    winner = models.CharField(max_length=100)
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
