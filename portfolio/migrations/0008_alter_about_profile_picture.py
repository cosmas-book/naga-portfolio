# Generated by Django 5.1.6 on 2025-02-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_about_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='profile_picture',
            field=models.ImageField(default='portfolio\\static\\images\\DSC_0032-removebg-preview (1).png', upload_to='profile_pics'),
        ),
    ]
