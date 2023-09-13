# Generated by Django 4.2.5 on 2023-09-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=128, unique=True)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('crea_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]