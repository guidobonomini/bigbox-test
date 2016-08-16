import datetime

from django.db import models
from django.db import connection
from django.utils import timezone

class Question(models.Model):
    #Question Model Fields
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    #Gets the recently published questions
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    #Choice Model Fields
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    #Execute function from db that gets 5 most voted polls
    #It excludes all polls with no votes
    def most_voted_polls():
        c = connection.cursor()
        try:
            c.execute("BEGIN")
            c.callproc("get_most_voted")
            results = c.fetchall()
        finally:
            c.close()
            return results
