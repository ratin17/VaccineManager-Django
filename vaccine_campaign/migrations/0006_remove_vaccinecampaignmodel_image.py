# Generated by Django 5.0.7 on 2024-07-14 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine_campaign', '0005_vaccinecampaignmodel_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinecampaignmodel',
            name='image',
        ),
    ]
