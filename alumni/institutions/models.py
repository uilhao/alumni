from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class InstitutionImageGallery(Orderable):
    """ Image Gallery """

    page = ParentalKey("institutions.InstitutionPage",
                       related_name="gallery_images"
                       )

    gallery_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        ImageChooserPanel("gallery_image")
    ]


class InstitutionListingPage(Page):
    """ Listing page """

    custom_title = models.CharField(
        max_length=100, null=False,
        blank=False,
        help_text='Title overwrite'
    )

    intro = RichTextField(blank=True, null=True)

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        FieldPanel('intro'),
    ]

    def get_context(self, request, *args, **kwargs):
        """ Custom """
        context = super().get_context(request, *args, **kwargs)
        context["institutions"] = InstitutionPage.objects.live().public()

        return context


class InstitutionPage(Page):
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
    sat_scores_average = models.IntegerField(blank=True, null=True)

    dapip_id = models.IntegerField(blank=True, null=True)
    ope_id = models.IntegerField(blank=True, null=True)

    # Relationships
    profile_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
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
            ImageChooserPanel("profile_image"),
        ], heading="Instituion Details"),
        FieldPanel('intro'),
        FieldPanel('about'),
        MultiFieldPanel([
            InlinePanel('gallery_images', max_num=8, min_num=0, label="Image"),
        ], heading="Image Gallery"),
    ]

    # Template
    template = "institutions/institutions_page.html"

    class Meta:
        verbose_name = "Institution Page"
        verbose_name_plural = "Institution Pages"
