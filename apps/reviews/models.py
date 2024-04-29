# from django.conf import settings
from django.db import models

# Create your models here.

# User = settings.AUTH_USER_MODEL

class RatingField(models.TextChoices):
    VERY_BAD = '1', 'Very Bad'
    BAD = '2', 'Bad'
    AVERAGE = '3', 'Average'
    GOOD = '4', 'Good'
    VERY_GOOD = '5', 'Very Good'

class Review(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    rater = models.CharField(max_length=100)
    rating = models.CharField(max_length=1, choices=RatingField.choices)
    comment = models.TextField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}"
    

    def get_average_rating(self):
        return Review.objects.filter(rating=self.rating).count()
    
    def get_rating_display(self):
        return dict(RatingField.choices)[self.rating]
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

