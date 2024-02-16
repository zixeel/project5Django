# Generated by Django 5.0.1 on 2024-01-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='students/', verbose_name='avatar')),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': ' студентики',
                'ordering': ('last_name',),
            },
        ),
    ]
