from django.db import models

# Create your models here
class Question(models.Model):           #each class represents a table structure/model
    ques_text=models.CharField(max_length=200)      #textfield for question
    pub_date=models.DateTimeField('Date published') #datetimefield for the publication datetime
    def __str__(self):
        return self.ques_text

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE) #this links/references the votes/choices to the corresponding questions. and the
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
