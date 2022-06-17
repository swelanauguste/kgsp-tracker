# Generated by Django 4.0.5 on 2022-06-17 12:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_ticket_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='uid',
            field=models.URLField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='uid',
            field=models.URLField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
