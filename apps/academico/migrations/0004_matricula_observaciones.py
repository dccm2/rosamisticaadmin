# Generated by Django 2.1.7 on 2019-04-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0003_curso_observaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='observaciones',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
