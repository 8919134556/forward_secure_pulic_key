# Generated by Django 3.2.8 on 2022-06-08 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0016_alter_request_file_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_file',
            name='status',
            field=models.CharField(blank=True, db_column='status', max_length=50, null=True, verbose_name='Status'),
        ),
    ]
