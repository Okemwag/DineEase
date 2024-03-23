#post-save signal for review model - recalculate average rating each time a new review is created

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Review
from django.core.exceptions import ValidationError

@receiver(post_save, sender=Review)
def update_average_rating(sender, instance, created, **kwargs):
    if created:
        reviews = Review.objects.filter(rating=instance.rating)
        average_rating = reviews.count()
        print(f"Average rating for {instance.get_rating_display()} is {average_rating}")
        return average_rating
    return None

# Pre-save signal for review model - check if user has already reviewed the product
@receiver(pre_save, sender=Review)
def check_duplicate_review(sender, instance, **kwargs):
    if Review.objects.filter(user=instance.user).exists():
        raise ValidationError("You have already reviewed this product")
    return None

