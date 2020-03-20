from django.db import models

# Create your models here.


from wagtail.core.models import Page
from wagtailgmaps.edit_handlers import MapFieldPanel

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel


class MapPage(Page):
    # template = "goom/goom_page.html"

    # Wagtailgmaps expects a `CharField` (or any other field that renders as a text input)
    formatted_address = models.CharField(max_length=255)
    latlng_address = models.CharField(max_length=255)

    # Use the `MapFieldPanel` just like you would use a `FieldPanel`
    content_panels = Page.content_panels + [
        MapFieldPanel('formatted_address'),
        MapFieldPanel('latlng_address', latlng=True),
    ]


    class Meta:
        verbose_name = 'Map Page'
        verbose_name_plural = 'Flex Pages'