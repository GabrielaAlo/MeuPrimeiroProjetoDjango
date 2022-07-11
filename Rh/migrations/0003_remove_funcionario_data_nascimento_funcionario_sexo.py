# Generated by Django 4.0.5 on 2022-06-29 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0002_depto_alter_funcionario_departamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='data_nascimento',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='sexo',
            field=models.CharField(blank=True, choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')], max_length=1, null=True),
        ),
    ]