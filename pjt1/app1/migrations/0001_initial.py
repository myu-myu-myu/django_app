# Generated by Django 4.2.8 on 2023-12-09 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('skater', models.CharField(max_length=100)),
                ('music', models.FileField(upload_to='music/files/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='music/covers/')),
            ],
        ),
    ]
