# Generated by Django 2.2.2 on 2019-06-19 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contasAlunos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='localDeTrab',
            field=models.TextField(blank=True, null=True),
        ),
    ]