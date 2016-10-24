from django import forms
from django_file_form.forms import FileFormMixin, UploadedFileField
from form_utils import forms as betterforms
from tinymce.widgets import TinyMCE
from django.forms.widgets import HiddenInput

# Form for creation of News 
class NewsForm(FileFormMixin, betterforms.BetterForm):
    name = forms.CharField()
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    image = UploadedFileField(required = False)
    form_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    upload_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    delete_url = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        fieldsets = [('main', {'fields': ['name',], 'legend': 'main', }),

                ('text-area', {'fields': ['body'], 'legend': 'text-area'}),
                ('images', {'fields': ['image'] + ['form_id', 'upload_url', 'delete_url'], 'legend': 'images'}),
                     ]
# Form for creations of Members
class MemberForm(FileFormMixin, betterforms.BetterForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    image = UploadedFileField(required = False)
    form_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    upload_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    delete_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    object_id = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        fieldsets = [('main', {'fields': ['first_name', 'last_name', ], 'legend': 'main', }),
                ('text-area', {'fields': ['description'], 'legend': 'text-area'}),
                ('images', {'fields': ['image'] + ['form_id', 'upload_url', 'delete_url'], 'legend': 'images'}),
                     ]

# Form for creations of Projects
### Categories for projets 
CATEGORIES = (('Дитячі Георгафії', 'Дитячі Георгафії'), ('Розвиток Територій', 'Розвиток Територій'))

class ProjectForm(FileFormMixin, betterforms.BetterForm):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, required = False)
    category = forms.ChoiceField(choices=CATEGORIES)
    image = UploadedFileField(required = False)
    form_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    upload_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    delete_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    object_id = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        fieldsets = [('main', {'fields': ['name', 'category', ], 'legend': 'main', }),
                ('text-area', {'fields': ['description'], 'legend': 'text-area'}),
                ('images', {'fields': ['image'] + ['form_id', 'upload_url', 'delete_url'], 'legend': 'images'}),
                     ]
# Form for creations of Partners 
class PartnerForm(FileFormMixin, betterforms.BetterForm):
    name = forms.CharField()
    image = UploadedFileField(required = False)
    form_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    upload_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    delete_url = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        fieldsets = [('main', {'fields': ['name',], 'legend': 'main', }),
                ('images', {'fields': ['image'] + ['form_id', 'upload_url', 'delete_url'], 'legend': 'images'}),
                     ]


