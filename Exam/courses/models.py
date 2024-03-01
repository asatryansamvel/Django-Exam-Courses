from django.db import models

class Course(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField(max_length = 500)
    rate = models.FloatField()
    count = models.IntegerField()

    def __str__(self):
        return self.title
