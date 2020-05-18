from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class InstitutionsPage(Page):
    """ Main Class """

    # Possible fields:
    # LocationName
    # LocationType
    # Address
    # GeneralPhone
    # AdminName
    # AdminPhone
    # AdminEmail
    # ProgramName
    # AccreditationDate
    # AccreditationStatus
    # DepartmentDescription

    # Database fields
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=400, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    accreditation_status = models.CharField(
        max_length=100, blank=True, null=True
    )
    intro = RichTextField(blank=True, null=True)
    about = RichTextField(blank=True, null=True)

    avg_gpa = models.FloatField(max_length=10, blank=True, null=True)
    sat_scores_average = models.FloatField(
        max_length=10, blank=True, null=True
    )

    # Relationships
    profile_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        # no special, just use field name
        related_name="+",
    )

    # Editor panels configuration
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('address'),
            FieldPanel('phone'),
            FieldPanel('accreditation_status'),
            FieldPanel('avg_gpa'),
            FieldPanel('sat_scores_average'),
        ]),
        FieldPanel('intro'),
        FieldPanel('about'),
        ImageChooserPanel("profile_image"),
    ]

    # Template
    template = "institutions/institutions_page.html"

    class Meta:
        verbose_name = "Institution Page"
        verbose_name_plural = "Institution Pages"
