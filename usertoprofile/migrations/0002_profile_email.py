# Generated by Django 2.1.7 on 2019-02-27 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertoprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='w@w.com', max_length=254),
            preserve_default=False,
        ),
    ]
