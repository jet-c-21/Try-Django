from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.id}. {self.title}"
