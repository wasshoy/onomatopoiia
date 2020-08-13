from django.db import models


class Odai(models.Model):
    odai_text = models.CharField(max_length=4)
    pub_date = models.DateTimeField('date published')


class Answer(models.Model):
    odai = models.ForeignKey(Odai, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

# class User(models.Model):
#     user_name = models.CharField(max_length=10)
