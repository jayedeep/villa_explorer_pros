from django import forms

class RecordNumberImport(forms.Form):
    number_of_records=forms.IntegerField()
