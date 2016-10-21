from django import forms
from django_file_form.forms import FileFormMixin, UploadedFileField
from form_utils import forms as betterforms
from tinymce.widgets import TinyMCE


CATEGORIES = (('Дитячі Георгафії', 'Дитячі Георгафії'), ('Розвиток Територій', 'Розвиток Територій'))

class ProjectForm(FileFormMixin, betterforms.BetterForm):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, required = False)
    category = forms.ChoiceField(choices=CATEGORIES)
    image = UploadedFileField(required = False)
    class Meta:
        fieldsets = [('main', {'fields': ['name', 'description', 'category', ], 'legend': 'main', }),
                ('images', {'fields': ['image'], 'legend': 'images'}),
                     ]
class NewsForm(FileFormMixin, betterforms.BetterForm):
    name = forms.CharField()
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    #body = forms.CharField(widget=forms.Textarea, required = False)
    picture = UploadedFileField(required = False)
    class Meta:
        fieldsets = [('main', {'fields': ['name', 'body', ], 'legend': 'main', }),
                ('images', {'fields': ['picture'], 'legend': 'images'}),
                     ]
class MemberForm(FileFormMixin, betterforms.BetterForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    avatar = UploadedFileField(required = False)
    class Meta:
        fieldsets = [('main', {'fields': ['first_name', 'last_name', 'description', ], 'legend': 'main', }),
                ('images', {'fields': ['avatar'], 'legend': 'images'}),
                     ]

