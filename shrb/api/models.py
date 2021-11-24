from django.contrib.auth.models import User
from django.db import models

from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Card(models.Model):
    user = models.ForeignKey(User, related_name='cards',on_delete=models.DO_NOTHING)
    date_from = models.DateField(blank=False)
    date_to = models.DateField(blank=False)
    description = models.TextField(blank=False)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return (self.user.username)