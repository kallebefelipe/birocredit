# Generated by Django 2.1 on 2018-08-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_auto_20180804_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=100, verbose_name='CEP'),
        ),
    ]
