from django import forms

class CommentForm(forms.Form):
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
    comment =   forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "name" : "comment",
            "class" : "form-control",
            "id" : "exampleFormControlTextarea1",
            "rows" : "3"
        }
    ))