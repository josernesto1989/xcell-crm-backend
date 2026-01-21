from django.db import models

class Tag(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    class Meta:
        unique_together = ('key', 'value')

    def __str__(self):
        return f"{self.key}: {self.value}"