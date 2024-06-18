from django.db import models
import uuid

# Create your models here.

class Memorial(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    qr_code_url = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return self.name