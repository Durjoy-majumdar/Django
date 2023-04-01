from django import forms

class InputForm(forms.Form):
    fname=forms.CharField(max_length=30)
    lname=forms.CharField(max_length=30)
    rollnumber=forms.IntegerField()
    password=forms.PasswordInput()
