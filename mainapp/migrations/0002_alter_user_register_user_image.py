# Generated by Django 3.2.8 on 2022-06-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_register',
            name='user_image',
            field=models.FileField(blank=True, db_column='user_image', upload_to='User/Profile-image/', verbose_name='User_Image'),
        ),
    ]