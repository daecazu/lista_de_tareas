"""Task model"""
from django.conf import settings
from django.db import models

class Task(models.Model):
    """Task model"""
    STATUS_CHOICES = [
        ('co','completa'),
        ('in','incompleta')
    ]
    PRIORITY_CHOICES = [
        ('b','baja'),
        ('m','media'),
        ('a','alta')
    ]
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    description = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='in',
    )
    priority = models.CharField(
        max_length=2,
        choices=PRIORITY_CHOICES,
        default='b',
    )

    def __str__(self):
        return self.name