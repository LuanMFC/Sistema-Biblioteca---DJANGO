from django.db.models.signals import pre_save
from django.dispatch import receiver
from Book.models import book
from openAI_API.client import get_book_synopsis


@receiver(pre_save, sender=book)
def Book_synopsis_pre_save(sender, instance, **kwargs):
    if not instance.synopsis:
        synopsis = get_book_synopsis(instance.title, instance.author, instance.publishing_company, instance.edition)
        instance.synopsis = synopsis