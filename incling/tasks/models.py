from django.db import models

class Tile(models.Model):
  STATUS_CHOICES = (
      ('live', 'live'),
      ('pending', 'pending'),
      ('archived', 'archived'),
  )
  date = models.DateField()
  status = models.CharField(max_length=10, choices=STATUS_CHOICES)



class Task(models.Model):
  TYPE_CHOICES = (
      ('survey', 'survey'),
      ('discussion', 'discussion'),
      ('diary', 'diary'),
  )
  title = models.CharField(max_length =255)
  order = models.PositiveIntegerField()
  type = models.CharField(max_length=10, choices=TYPE_CHOICES)
  description = models.TextField()
  tile = models.ForeignKey(Tile, on_delete=models.CASCADE)

