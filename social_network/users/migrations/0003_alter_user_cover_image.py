# Generated by Django 4.2.5 on 2023-09-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cover_image',
            field=models.ImageField(default='user/profile_picture', upload_to='users/covers'),
        ),
    ]