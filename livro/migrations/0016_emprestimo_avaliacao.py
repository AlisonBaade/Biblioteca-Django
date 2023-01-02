# Generated by Django 4.1.4 on 2022-12-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0015_alter_emprestimo_nome_emprestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='avaliacao',
            field=models.CharField(choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
