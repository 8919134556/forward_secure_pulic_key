# Generated by Django 3.2.8 on 2022-06-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_upload_file_request_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_file',
            name='request_mail',
            field=models.EmailField(blank=True, db_column='request_mail', max_length=100, null=True, verbose_name='Request_Mail'),
        ),
    ]
