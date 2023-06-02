from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    project_key = models.IntegerField(default=False)

    def __str__(self):
        return self.tittle + ' - ' + self.project.name