# Generated by Django 2.0.6 on 2019-06-28 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeelist',
            name='headpic',
            field=models.ImageField(default=2, upload_to='pics'),
            preserve_default=False,
        ),
    ]
