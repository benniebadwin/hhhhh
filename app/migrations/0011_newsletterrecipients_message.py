# Generated by Django 4.1.7 on 2023-04-04 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_product_image4_remove_product_image5'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletterrecipients',
            name='message',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]