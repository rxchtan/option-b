from django.db import models

class Headline(models.Model):
  title = models.CharField(max_length=200)
  url = models.TextField()
  text = models.TextField()

  def __str__(self):
    return self.title

class History(models.Model):
  title = models.CharField(max_length=200)
  url = models.TextField()
  text = models.TextField()

  def __str__(self):
    return self.title

