from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    first_name = None
    last_name = None
    last_login = None

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-id"]

class WaitingUser(models.Model):
    email = models.EmailField(unique=True)
    referrer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    deletion_confirmation_code = models.CharField(max_length=7, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-id"]

class Recommendation(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    recommended_person = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.recommended_person}"

    class Meta:
        ordering = ["-id"]

class FAQuestion(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.order}. {self.question}"

    class Meta:
        verbose_name = "FAQuestion"
