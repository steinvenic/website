# Generated by Django 2.0.8 on 2019-02-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_article',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]