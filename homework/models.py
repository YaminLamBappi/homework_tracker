from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
      return self.tag_name
  
class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    homework_task = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    due_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
      return self.homework_task


class Notes(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  subject = models.CharField(max_length=255, null=True, blank=True)
  note = models.CharField(max_length=233, blank=False)
  file = models.FileField()
  date = models.DateField()

  def __str__(self) :
     return self.note