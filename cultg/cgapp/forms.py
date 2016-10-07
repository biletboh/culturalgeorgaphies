from django import forms
from django_file_form.forms import FileFormMixin, UploadedFileField

CATEGORIES = (('Дитячі Георгафії', 'Дитячі Георгафії'), ('Розвиток Територій', 'Розвиток Територій'))

class ProjectForm(FileFormMixin, forms.Form):
    name = forms.CharField()
    name = forms.CharField()
    description = forms.CharField()
    category = forms.ChoiceField(choices=CATEGORIES)
    image = UploadedFileField(required = False)

