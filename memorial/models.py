from django.db import models
import uuid
from django.urls import reverse

# Create your models here.

class Memorial(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    qr_code_url = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('view_memorial', args=[str(self.unique_id)])