from django.db import models

# Create your models here.
class ToDoItems(models.Model):
    title=models.CharField(max_length=255)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title
