# Generated by Django 4.2.1 on 2023-06-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
    ]