# Generated by Django 4.1 on 2023-05-14 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homerental", "0002_profile_is_homeowner"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="location",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="phone",
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]