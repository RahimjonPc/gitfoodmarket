# Generated by Django 3.1.2 on 2020-10-21 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foods',
            options={'verbose_name_plural': 'Foods'},
        ),
        migrations.AddField(
            model_name='foods',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]
