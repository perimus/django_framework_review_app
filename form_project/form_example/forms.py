from django import forms

RADIO_CHOICES = (
    ("Value One", "Value One Display"),
    ("Value Two", "Text for Value Two"),
    ("Value Three", "Value Three's Display Text"),
)

BOOK_CHOICES = (
    ("Non-Fiction", (("1", "Deep Learnig With Keras"), ("2", "Web Development with Django"))),
    ("Fiction", (("3", "Brave New world"), ("4", "The Great Gatsby"))),
)


class ExampleForm(forms.Form):
    text_input = forms.CharField(max_length=3)
    password_input = forms.CharField(widget=forms.PasswordInput, min_length=8)
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    favorite_book = forms.ChoiceField(choices=BOOK_CHOICES)
    books_you_own = forms.MultipleChoiceField(required=False, choices=BOOK_CHOICES)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField(min_value=1, max_value=10)
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField(max_digits=5, decimal_places=3)
    email_input = forms.EmailField()
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")


class NewsletterSignupForm(forms.Form):

    signup = forms.BooleanField(label="Sign up to newsletter?", required=False)

    email = forms.EmailField(help_text="Enter your email address to subscribe", required=False)

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data["signup"] and not cleaned_data.get("email"):
            self.add_error("email", "Your email address is required if signing up for the newsletter.")

class OrderForm(forms.Form):
    item_a = forms.IntegerField(min_value=0, max_value=100)
    item_b = forms.IntegerField(min_value=0, max_value=100)
    
    def clean(self) -> None:
        cleaned_data = super().clean()
        if cleaned_data.get("item_a", 0) + cleaned_data.get("item_b", 0) > 100:
            self.add_error(None, "The total number of items must be 100 or less.")