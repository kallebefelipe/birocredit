# Generated by Django 2.1 on 2018-08-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='fonte_renda',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='fonte_renda'),
        ),
    ]