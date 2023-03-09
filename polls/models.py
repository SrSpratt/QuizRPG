from django.db import models
from django.utils import timezone
import datetime

class Maps(models.Model):
    maps_text = models.CharField(max_length=50)
    difficulty = models.IntegerField(default=1)
    accesses = models.IntegerField(default=0)
    def __str__(self):
        return self.maps_text
    def is_difficult(self):
        return self.difficulty > 5
    class Meta:
        verbose_name = 'Mapa'


class Question(models.Model):
    maps = models.ForeignKey(Maps, null=True, blank=True, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name = 'Escolha'
    

# Create your models here.
