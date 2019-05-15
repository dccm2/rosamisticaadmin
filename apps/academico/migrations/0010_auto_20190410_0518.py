# Generated by Django 2.1.7 on 2019-04-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0009_auto_20190410_0440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='inscrito',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='ugel',
        ),
        migrations.AddField(
            model_name='inscrito',
            name='asesora',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='inscrito',
            name='beneficiario',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inscrito',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='academico.Curso'),
        ),
        migrations.AddField(
            model_name='inscrito',
            name='descuento_actual',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='inscrito',
            name='descuento_pendiente',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='inscrito',
            name='fecha_diploma',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='inscrito',
            name='fecha_matricula',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='inscrito',
            name='modulos_entregados',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='inscrito',
            name='promocion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='inscrito',
            name='ugel',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='academico.Ugel'),
        ),
        migrations.DeleteModel(
            name='Matricula',
        ),
    ]
