# Generated by Django 2.1.7 on 2019-04-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0008_auto_20190410_0415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='curso',
        ),
        migrations.AddField(
            model_name='matricula',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='academico.Curso'),
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='inscrito',
        ),
        migrations.AddField(
            model_name='matricula',
            name='inscrito',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='academico.Inscrito'),
        ),
    ]
