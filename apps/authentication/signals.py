# signals.py
from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from django.shortcuts import redirect


@receiver(email_confirmed)
def email_confirmed_redirect(sender, request, email_address, **kwargs):
    user = email_address.user
    if user.is_admin:
        return redirect('admin_dashboard')  
    else:
        return redirect('user_dashboard')  
