# Generated by Django 2.2.28 on 2024-03-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipbook', '0004_flipbookdownload_download_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='flipbook',
            name='password',
            field=models.CharField(blank=True, max_length=64, verbose_name='Password'),
        ),
    ]