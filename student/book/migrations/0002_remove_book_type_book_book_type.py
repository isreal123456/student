# Generated by Django 4.2 on 2023-08-12 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="book", name="type",),
        migrations.AddField(
            model_name="book",
            name="book_type",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="book.book_types",
            ),
            preserve_default=False,
        ),
    ]
