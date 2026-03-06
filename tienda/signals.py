
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Documento

@receiver(post_save,sender=Documento )
def registrar_cambio(sender, instance, created, **kwargs):
    if created:
        print(f"Documento creado: {instance.titulo}")
    else:
        print(f"Documento actualizado: {instance.titulo}")

@receiver(post_delete,sender=Documento )
def registrar_delete(sender, instance, **kwargs):
        print(f"Documento eliminado: {instance.titulo}")