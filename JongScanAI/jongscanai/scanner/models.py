from django.db import models

class ScanResult(models.Model):
    url = models.URLField()
    risk = models.CharField(max_length=50)
    description = models.TextField()
    solution = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
