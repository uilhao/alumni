""" Root Pages """

from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from streams import blocks


class RootPage(Page):
    """ Root page class """

    template = "root/root_page.html"

    # Page Content
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("richtext", blocks.RichTextBlock()),
            ("cards", blocks.CardBlock()),
        ],
        null=True,
        blank=True,
    )

    # Admin
    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]


class Meta:
    verbose_name = "Root Pages"
    verbose_name_plural = "Root Pages"
