from django.contrib import auth
from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    DateTimeField,
    EmailField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    Model,
    TextChoices,
    TextField,
    URLField,
)


class DBContributor(Model):
    """
    A contributor to a book, e.g. author, editor, co-author.
    """

    first_name = CharField(max_length=32, help_text="The contributor's first name.")
    middle_names = CharField(null=True, max_length=64, help_text="The contributor's middle name or names.")
    last_name = CharField(max_length=32, help_text="The contributor's last name.")

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        db_table = "contributors"


class DBContributor(Model):
    """
    A contributor to a book, e.g. author, editor, co-author.
    """

    first_name = CharField(max_length=32, help_text="The contributor's first name.")
    middle_names = CharField(null=True, max_length=64, help_text="The contributor's middle name or names.")
    last_name = CharField(max_length=32, help_text="The contributor's last name.")
    email = CharField(null=True, max_length=320, help_text="The contributor's email address.")

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        db_table = "contributors"


class DBPublisher(Model):
    """
    A company that publishes books.
    """

    name = CharField(max_length=112, help_text="The name of the publisher.")
    website = URLField(null=True, max_length=2000, help_text="The publisher's website.")
    email = EmailField(null=True, max_length=320, help_text="The publisher's email address.")

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "publishers"


class DBReview(Model):
    """
    A review of a book.
    """

    content = TextField(help_text="The content of the review.")
    rating = IntegerField(help_text="The rating the reviewer has given.")
    date_created = DateTimeField(auto_now_add=True, help_text="The date and time this review was created.")
    date_edited = DateTimeField(null=True, help_text="The date and time this review was edited.")
    creator = ForeignKey(auth.get_user_model(), on_delete=CASCADE)
    book = ForeignKey("DBBook", on_delete=CASCADE, help_text="The book that this review is for.")

    class Meta:
        db_table = "reviews"


class DBBook(Model):
    """A published book."""

    title = CharField(max_length=70, help_text="The title of the book.")
    publication_date = DateField(verbose_name="Date the book was published.")
    isbn = CharField(max_length=20, verbose_name="ISBN number of the book.")
    publisher = ForeignKey("DBPublisher", on_delete=CASCADE)
    contributors = ManyToManyField("DBContributor", through="DBBookContributor")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "books"


class DBBookContributor(Model):
    class ContributionRoles(TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-author"
        EDITOR = "EDITOR", "Editor"
        COMMENTATOR = "COMMENTATOR", "Commentator"

    book = ForeignKey("DBBook", on_delete=CASCADE)
    contributor = ForeignKey("DBContributor", on_delete=CASCADE)
    role = CharField(
        verbose_name="The role this contributor had in the book", choices=ContributionRoles.choices, max_length=20
    )

    class Meta:
        db_table = "books_contributors"
