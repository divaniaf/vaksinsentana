from django import forms

class userinput(forms.Form):
    jmlTwt = forms.IntegerField(required=True, label='Input Jumlah')