from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CategoriesConfig(AppConfig):
    name = "osmweb.categories"
    verbose_name = _("Categories")

    def ready(self):
        try:
            from osmweb import categories
        except ImportError:
            pass
