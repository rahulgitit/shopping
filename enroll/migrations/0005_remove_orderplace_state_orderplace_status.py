# Generated by Django 5.0 on 2024-01-09 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0004_rename_status_orderplace_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplace',
            name='state',
        ),
        migrations.AddField(
            model_name='orderplace',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='panding', max_length=100),
        ),
    ]