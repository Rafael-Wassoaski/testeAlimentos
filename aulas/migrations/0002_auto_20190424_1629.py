# Generated by Django 2.0.13 on 2019-04-24 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='aulas',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='aulas',
            name='conteudo',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aulas',
            name='video',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aulas',
            name='assuntos',
            field=models.CharField(choices=[('ECA', 'ENTENDENDO A CONTAMINAÇÃO DOS ALIMENTOS'), ('AMA', 'AMBIENTE DE MANIPULAÇÃO E CUIDADOS COM ÁGUA'), ('MLV', 'MANUSEIO DO LIXO E CONTROLE DE VETORES E PRAGAS'), ('HIG', 'HIGIENIZAÇÃO'), ('MEV', 'MANIPULADORES E VISITANTES'), ('EDM', 'ETAPAS DA MANIPULAÇÃO'), ('DOC', 'DOCUMENTAÇÃO')], default='ECA', max_length=2),
        ),
        migrations.AddField(
            model_name='comentario',
            name='aula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas.Aulas'),
        ),
    ]
