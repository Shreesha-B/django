from django import forms


class Info(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    range = forms.IntegerField()
