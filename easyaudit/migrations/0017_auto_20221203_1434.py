# Generated by Django 3.2.15 on 2022-12-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyaudit', '0016_alter_crudevent_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crudevent',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date time'),
        ),
        migrations.AlterField(
            model_name='loginevent',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date time'),
        ),
        migrations.AlterField(
            model_name='requestevent',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date time'),
        ),
    ]
