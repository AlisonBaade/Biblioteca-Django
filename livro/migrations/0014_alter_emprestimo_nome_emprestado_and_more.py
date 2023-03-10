# Generated by Django 4.1.4 on 2022-12-21 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0013_remove_emprestimo_tempo_duracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_emprestado',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_emprestado_anonimo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
