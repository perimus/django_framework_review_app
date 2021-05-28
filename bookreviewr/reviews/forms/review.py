from django import forms

from ..models import DBReview

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=0, max_value=5)
    
    class Meta:
        model = DBReview
        fields = "__all__"
        exclude = ["book", "date_edited"]
