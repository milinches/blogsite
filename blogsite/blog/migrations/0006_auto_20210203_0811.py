# Generated by Django 3.1.6 on 2021-02-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_articles_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='body',
            field=models.TextField(),
        ),
    ]