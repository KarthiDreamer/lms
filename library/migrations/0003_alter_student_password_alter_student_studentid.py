# Generated by Django 4.1.3 on 2022-12-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_books_bookauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
