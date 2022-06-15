# Generated by Django 3.2.8 on 2022-06-08 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_upload_file_screat_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request_file',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_id', models.CharField(blank=True, db_column='file_id', max_length=50, null=True, verbose_name='File_Id')),
                ('file_name', models.CharField(blank=True, db_column='file_name', max_length=50, null=True, verbose_name='File_Name')),
                ('file_type', models.CharField(blank=True, db_column='file_type', max_length=50, null=True, verbose_name='File_Type')),
                ('file_size', models.TextField(blank=True, db_column='file_size', null=True, verbose_name='File_Size')),
                ('screat_key', models.TextField(blank=True, db_column='screat_key', max_length=100, null=True, verbose_name='Screat_Key')),
                ('Key', models.TextField(blank=True, db_column='key', max_length=500, null=True, verbose_name='Key')),
                ('status', models.CharField(blank=True, db_column='status', max_length=50, null=True, verbose_name='Status')),
            ],
            options={
                'db_table': 'Request_file',
            },
        ),
    ]
