from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, Waiter


@receiver(post_save, sender=CustomUser)
def create_restraunt_manager(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_restraunt_manager(sender, instance, **kwargs):
    instance.user.save()


@receiver(post_save, sender=Waiter)
def create_waiter(sender, instance, created, **kwargs):
    if created:
        Waiter.objects.create(user=instance)


@receiver(post_save, sender=Waiter)
def save_waiter(sender, instance, **kwargs):
    instance.user.save()