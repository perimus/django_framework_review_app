# Generated by Django 3.2.3 on 2021-05-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_dbcontributor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbbookcontributor',
            name='role',
            field=models.CharField(choices=[('AUTHOR', 'Author'), ('CO_AUTHOR', 'Co-author'), ('EDITOR', 'Editor'), ('COMMENTATOR', 'Commentator')], max_length=20, verbose_name='The role this contributor had in the book'),
        ),
    ]