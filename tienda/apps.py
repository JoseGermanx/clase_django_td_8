from django.apps import AppConfig


class TiendaConfig(AppConfig):
    name = 'tienda'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import tienda.signals
