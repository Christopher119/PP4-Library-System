# Generated by Django 4.2.17 on 2025-01-12 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_options_alter_review_options_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_content',
            field=models.TextField(blank=True),
        ),
    ]
