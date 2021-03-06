# Generated by Django 2.1.5 on 2019-02-10 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0006_remove_curtida_curtidas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=400)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meus_comentarios', to='perfis.Perfil')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meus_comentarios', to='perfis.Postagem')),
            ],
        ),
    ]
