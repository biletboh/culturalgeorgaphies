from django import forms
from django_file_form.forms import FileFormMixin, UploadedFileField
from form_utils import forms as betterforms
from tinymce.widgets import TinyMCE
from django.forms.widgets import HiddenInput
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from datetimewidget.widgets import DateTimeWidget

## Language choices 
LANGUAGES = (('English', 'English'), ('Українська', 'Українська'))

# Form for creation of News 
class NewsForm(FileFormMixin, betterforms.BetterForm):
    name = forms.CharField(label=_("name"), max_length=200)
    language = forms.ChoiceField(label=_("language"), choices=LANGUAGES)
    pub_date = forms.DateTimeField(label=_("publication date"), widget=DateTimeWidget(usel10n=True, bootstrap_version=3), initial=timezone.now)
    body = forms.CharField(label=_("body"), widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    image = UploadedFileField(label=_("image"), required = False)
    form_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    upload_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    delete_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    object_id = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        fieldsets = [('main', {'fields': ['name', 'language', 'pub_date'], 'legend': 'main', }),

                ('text-area', {'fields': ['body'], 'legend': 'text-area'}),
                ('images', {'fields': ['image'] + ['form_id', 'upload_url', 'delete_url'], 'legend': 'images'}),
                     ]
# Form for creations of Members
class MemberForm(FileFormMixin, betterforms.BetterForm):
    first_name = forms.CharField(label=_("first name"), max_length=200)
    last_name = forms.CharField(label=_("last name"), max_length=200)
    language = forms.ChoiceField(label=_("language"), choices=LANGUAGES)
    pub_date = forms.DateTimeField(label=_("publication date"), widget=DateTimeWidget(usel10n=True, bootstrap_version=3), initial=timezone.now)
    description = forms.CharField(label=_("description"), widget=TinyMCE(attrs={'cols': 80, 'rows': 15}), required=False)
    image = UploadedFileField(label=_("image"), required = False)
    form_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    upload_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    delete_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    object_id = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        fieldsets = [('main', {'fields': ['first_name', 'last_name', 'language', 'pub_date'], 'legend': 'main', }),
                ('text-area', {'fields': ['description'], 'legend': 'text-area'}),
                ('images', {'fields': ['image'] + ['form_id', 'upload_url', 'delete_url'], 'legend': 'images'}),
                     ]

# Form for creations of Projects

### Categories for projets 
CATEGORIES = (("Children's geographies", _("Children's geographies")), ('Development of territories', _('Development of territories')))

class ProjectForm(FileFormMixin, betterforms.BetterForm):
    name = forms.CharField(label=_("name"), max_length=200)
    category = forms.ChoiceField(label=_("category"), choices=CATEGORIES)
    language = forms.ChoiceField(label=_("language"), choices=LANGUAGES)
    pub_date = forms.DateTimeField(label=_("publication date"), widget=DateTimeWidget(usel10n=True, bootstrap_version=3), initial=timezone.now)
    description = forms.CharField(label=_("description"), widget=TinyMCE(attrs={'cols': 80, 'rows': 15}), required=False)
    image = UploadedFileField(label=_("image"), required = False)
    form_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    upload_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    delete_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    object_id = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        fieldsets = [('main', {'fields': ['name', 'category', 'language', 'pub_date'], 'legend': 'main', }),
                ('text-area', {'fields': ['description'], 'legend': 'text-area'}),
                ('images', {'fields': ['image'] + ['form_id', 'upload_url', 'delete_url'], 'legend': 'images'}),
                     ]
# Form for creations of Partners 
class PartnerForm(FileFormMixin, betterforms.BetterForm):
    name = forms.CharField(label=_("name"), max_length=200)
    image = UploadedFileField(label=_("image"), required = False)
    form_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    upload_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    delete_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    object_id = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        fieldsets = [('main', {'fields': ['name', ], 'legend': 'main', }),
                ('images', {'fields': ['image'] + ['form_id', 'upload_url', 'delete_url'], 'legend': 'images'}),
                     ]

