# Generated by Django 3.2.8 on 2022-06-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_upload_file_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_file',
            name='request_mail',
            field=models.EmailField(blank=True, db_column='Request_Mail', max_length=100, null=True, verbose_name='request_mail'),
        ),
    ]
