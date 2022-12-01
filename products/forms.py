from django import forms

class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=150)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField(min_value=0)


class CommentCreateForm(forms.Form):
    text = forms.CharField(min_length=1, max_length=150)



