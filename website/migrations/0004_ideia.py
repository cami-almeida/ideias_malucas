# Generated by Django 2.2.3 on 2019-07-28 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_pessoa_senha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ideia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True, verbose_name='Nome de ideia')),
                ('descricao', models.TextField(verbose_name='Descreva sua ideia')),
                ('categorias', models.CharField(choices=[('TECNOLOGIA', 'Tecnologia'), ('CIENCIA', 'Ciência'), ('ESPORTE', 'Esporte'), ('OUTROS', 'Outros')], max_length=255, verbose_name='Categorias')),
                ('categoria_outros', models.CharField(blank=True, max_length=255, null=True, verbose_name='Caso outros, qual?')),
                ('data_de_criacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('pessoa', models.ForeignKey(on_delete=None, to='website.Pessoa')),
            ],
        ),
    ]