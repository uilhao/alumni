from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class HomePage(Page):
    """ Main Class """

    max_count = 1

    # Database fields
    body = RichTextField(blank=True, null=True)
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(
        features=["bold", "italic"], blank=True, null=True
    )

    # Relationships
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        # no special, just use field name
        related_name="+",
    )

    banner_call_to_action = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        # no special, just use field name
        related_name="+",
    )

    # Editor panels configuration
    content_panels = Page.content_panels + [
        # FieldPanel('date'),
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_call_to_action"),
    ]

    # Template
    template = "home/home_page.html"

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)

        context['menuitems'] = self.get_children()
        # .filter(live=True, show_in_menus=True)

        return context

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
