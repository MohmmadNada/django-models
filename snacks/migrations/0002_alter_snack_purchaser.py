# Generated by Django 3.2.5 on 2021-07-12 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='purchaser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
