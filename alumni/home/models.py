from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

class HomePage(Page):
    """ Main Class """

    # Database fields
    body = RichTextField(blank=True, null=True)

    # Editor panels configuration
    content_panels = Page.content_panels + [
        # FieldPanel('date'),
        FieldPanel('body', classname="full"),
    ]

    # Template
    template = "home/home_page.html"


    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)

        context['menuitems'] = self.get_children()
        # .filter(live=True, show_in_menus=True)

        return context


    class Meta:
        verbose_name = "AlumniShip"
        verbose_name_plural = "AlumniShips"
