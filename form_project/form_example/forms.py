from django import forms
from django.core.exceptions import ValidationError


def validate_email_domain(value: str) -> None:
    if value.split("@")[-1].lower() != "example.com":
        raise ValidationError("The email address must be on the domain example.com.")


class OrderForm(forms.Form):
    magazine_count = forms.IntegerField(min_value=0, max_value=80, widget=forms.NumberInput(attrs={"placeholder": "Number of Magazines"}))
    book_count = forms.IntegerField(min_value=0, max_value=50, widget=forms.NumberInput(attrs={"placeholder": "Number of Books"}))
    send_confirmation = forms.BooleanField(required=False)
    email = forms.EmailField(required=False, validators=[validate_email_domain], widget=forms.EmailInput(attrs={"placeholder": "Your company email address"}))

    def clean_email(self) -> str:
        return self.cleaned_data["email"].lower()

    def clean(self) -> None:
        cleaned_data = super().clean()

        if cleaned_data.get("send_confirmation") and not cleaned_data.get("email"):
            self.add_error("email", "Please provide your email address to receive the confirmation message.")
        elif cleaned_data.get("email") and not cleaned_data.get("send_confirmation"):
            self.add_error("send_confirmation", "Please check this if you want to receive a confirmaton mail.")

        if cleaned_data.get("magazine_count", 0) + cleaned_data.get("book_count", 0) > 100:
            self.add_error(None, "The total amount of items must be 100 or less.")
