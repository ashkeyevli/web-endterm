from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = '_auth'

    def ready(self):
        import _auth.signals

