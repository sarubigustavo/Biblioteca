from django import forms

class CreateBookForm(forms.Form):
    isbn = forms.IntegerField()
    title = forms.CharField(max_length=20)
    author = forms.CharField(max_length=20)
    #edition = forms.DateField(required=False)
    edition = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}), input_formats=('%d/%m/%Y', ))

class FindBookForm(forms.Form):
    title = forms.CharField(max_length=20, required=False)