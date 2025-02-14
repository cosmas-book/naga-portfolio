# Generated by Django 5.1.6 on 2025-02-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(upload_to='images/')),
                ('email', models.EmailField(max_length=254)),
                ('linkedin_url', models.URLField(max_length=500)),
                ('instagram_url', models.URLField(max_length=500)),
                ('x_url', models.URLField(max_length=500)),
                ('facebook_url', models.URLField(max_length=500)),
            ],
        ),
    ]
