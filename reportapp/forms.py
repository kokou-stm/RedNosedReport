from django import forms

class ReportForm(forms.Form):
    text_input = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}),
        required=False,
        label="Saisir les rapports manuellement "
    )
    file_input = forms.FileField(
        required=False,
        label="Uploader un fichier (.txt)"
    )

    def clean(self):
        cleaned_data = super().clean()
        text_input = cleaned_data.get('text_input')
        file_input = cleaned_data.get('file_input')

        if not text_input and not file_input:
            raise forms.ValidationError("Veuillez fournir soit du texte, soit un fichier.")
        return cleaned_data