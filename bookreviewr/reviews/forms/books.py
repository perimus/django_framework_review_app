from django import forms


class SearchForm(forms.Form):
    """"""

    SEARCH_CHOICES = (
        ("title", "Title"),
        ("contributor", "Contributor"),
    )

    search = forms.CharField(min_length=3, required=False)
    search_in = forms.ChoiceField(choices=SEARCH_CHOICES, required=False)
