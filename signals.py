from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import RSVP

@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    ...

@receiver(post_save, sender=RSVP)
def send_rsvp_confirmation(sender, instance, created, **kwargs):
    ...
