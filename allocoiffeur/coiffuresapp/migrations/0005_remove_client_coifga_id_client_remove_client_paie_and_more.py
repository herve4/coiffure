# Generated by Django 4.2.2 on 2023-09-22 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coiffuresapp', '0004_alter_client_telephone_cl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='coifGa_id_client',
        ),
        migrations.RemoveField(
            model_name='client',
            name='paie',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coiffuresapp.client', verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email_cl',
            field=models.EmailField(blank=True, max_length=50, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='nom_cl',
            field=models.CharField(max_length=25, verbose_name='Nom'),
        ),
    ]