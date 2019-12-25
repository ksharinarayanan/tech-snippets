from django import forms

class CommentForm(forms.Form):
    name    =   forms.CharField(label='Name')
    email   =   forms.EmailField()
    comment =   forms.CharField(widget=forms.Textarea(
        attrs={
            "class" : "form-control",
            "id" : "exampleFormControlTextarea1",
            "rows" : "3"
        }
    ))