from django import forms

CATEGORIES = (('Дитячі Георгафії', 'Дитячі Георгафії'), ('Розвиток Територій', 'Розвиток Територій'))

class ProjectForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    category = forms.ChoiceField(choices=CATEGORIES)
