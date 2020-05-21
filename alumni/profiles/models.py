from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


# TODO Added Alumni page type and look into getting more data from linkedin api
# https://developer.linkedin.com/docs/rest-api

# hidden form to submit about section of institution


class ProfileListingPage(Page):
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
        context["profiles"] = ProfilePage.objects.live().public()

        return context


class ProfilePage(Page):
    """ Main Class """

    # Database fields
    name = models.CharField(max_length=200, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)

    intro = RichTextField(blank=True, null=True)
    about = RichTextField(blank=True, null=True)

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
            FieldPanel('school'),
            ImageChooserPanel("profile_image"),
        ], heading="Profile Details"),
        FieldPanel('intro'),
        FieldPanel('about'),
        MultiFieldPanel([
            InlinePanel('degrees', max_num=8, min_num=0, label="Degree"),
        ], heading="Degrees"),
        MultiFieldPanel([
            InlinePanel('career_history', max_num=8,
                        min_num=0, label="Career History"),
        ], heading="Career History"),
    ]

    # Template
    template = "profiles/profiles_page.html"

    class Meta:
        verbose_name = "Profile Page"
        verbose_name_plural = "Profiles Pages"


class ProfileDegrees(Orderable):
    """ Degrees """

    page = ParentalKey(ProfilePage, related_name='degrees')
    institution_name = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, null=True, blank=True)
    majors = models.CharField(max_length=255, null=True, blank=True)
    year_start = models.CharField(max_length=255, null=True, blank=True)
    year_graduated = models.CharField(max_length=255, null=True, blank=True)

    panels = [
        FieldPanel('institution_name'),
        FieldPanel('degree'),
        FieldPanel('majors'),
        FieldPanel('year_start'),
        FieldPanel('year_graduated'),
    ]


class ProfileCareerHistory(Orderable):
    """ Career History """

    page = ParentalKey(ProfilePage, related_name='career_history')
    company_name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    year_start = models.CharField(max_length=255, null=True, blank=True)
    year_departed = models.CharField(max_length=255, null=True, blank=True)

    panels = [
        FieldPanel('company_name'),
        FieldPanel('position'),
        FieldPanel('year_start'),
        FieldPanel('year_departed'),
    ]
