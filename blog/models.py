from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('diary', '영어일기'),
        ('speaking', '영어회화'),
        ('personal_feedback', '학습점검'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='diary'
    )
    
    def __str__(self):
        return self.title