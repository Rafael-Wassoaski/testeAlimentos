# Generated by Django 2.0.13 on 2019-06-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0007_auto_20190612_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
