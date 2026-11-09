from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Subject(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education = models.TextField()
    experience = models.IntegerField()
    bio = models.TextField()
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    subjects = models.ManyToManyField(Subject)

class Booking(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_bookings')
    tutor = models.ForeignKey(TutorProfile, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='pending')

class Review(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    tutor = models.ForeignKey(TutorProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
