# Generated by Django 4.1.1 on 2022-11-17 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0007_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
