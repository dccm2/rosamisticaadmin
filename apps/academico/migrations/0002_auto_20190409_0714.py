# Generated by Django 2.1.7 on 2019-04-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='decuento_actual',
            new_name='descuento_actual',
        ),
        migrations.AddField(
            model_name='matricula',
            name='modulos_entregados',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='direccion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
