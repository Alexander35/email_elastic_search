from .models import Email
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Email)
def index_email(sender, instance, **kwarkgs):
	print('Email Indexed')
	instance.indexing()