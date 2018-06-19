# Generated by Django 2.0.6 on 2018-06-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookflood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='books_wanted',
            field=models.ManyToManyField(related_name='want_it', to='bookflood.Book'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='books_read',
            field=models.ManyToManyField(related_name='read_it', to='bookflood.Book'),
        ),
    ]
