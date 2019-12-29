from django import forms

class ReplyForm(forms.Form):
    name    =   forms.CharField(widget=forms.TextInput(
        attrs={
            "name" : "name",
            "class" : "form-control",
            "id" : "exampleFormControlInput1",
        }
    ))
    email   =   forms.EmailField(widget=forms.TextInput(
        attrs={
            "name" : "email",
            "class" : "form-control",
            "id" : "exampleFormControlInput1",
        }
    ))
    comment   =   forms.CharField(widget=forms.Textarea(
        attrs={
            "name" : "reply",
            "class" : "form-control",
            "id" : "exampleFormControlTextarea1",
            "rows" : "3"
        }
    ))