from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import AccountBalance

@receiver(post_save, sender=User)
def create_account_balance(sender, instance, created, **kwargs):
    if created:
        AccountBalance.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_account_balance(sender, instance, **kwargs):
    instance.accountbalance.save()

