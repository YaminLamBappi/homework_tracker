from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  subject = models.CharField(max_length=255, null=True, blank=True)
  note = models.CharField(max_length=233, blank=False)
  file = models.FileField()
  date = models.DateField()

  def __str__(self) :
     return self.note