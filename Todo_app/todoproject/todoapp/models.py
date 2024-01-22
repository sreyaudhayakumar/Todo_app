from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    time = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)  

    def __str__(self):
        return self.title