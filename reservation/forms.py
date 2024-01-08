from django import forms

class TrainSearchForm(forms.Form):
    from_stop = forms.CharField()
    to_stop = forms.CharField()
    selected_date = forms.DateField(label='Select Date', widget=forms.SelectDateWidget)

class BookingForm(forms.Form):
    name = forms.CharField(max_length=255)
    age = forms.IntegerField()