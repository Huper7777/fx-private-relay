# Generated by Django 2.2.13 on 2021-01-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0012_profile_num_address_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="last_hard_bounce",
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="last_soft_bounce",
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
