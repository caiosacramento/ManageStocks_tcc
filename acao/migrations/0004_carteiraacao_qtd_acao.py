# Generated by Django 4.0.3 on 2023-10-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acao', '0003_remove_acao_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='carteiraacao',
            name='qtd_acao',
            field=models.IntegerField(default=1, verbose_name='quantidade de ação'),
        ),
    ]
