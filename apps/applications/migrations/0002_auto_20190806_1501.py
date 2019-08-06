# Generated by Django 2.1.7 on 2019-08-06 07:01

import common.fields.model
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('login_mode', models.CharField(choices=[('auto', 'Automatic login'), ('manual', 'Manually login')], default='auto', max_length=10, verbose_name='Login mode')),
                ('type', models.CharField(choices=[('mysql', 'MySQL')], default='mysql', max_length=10, verbose_name='Type')),
                ('host', models.CharField(max_length=128, verbose_name='Host')),
                ('port', models.IntegerField(default=3306, verbose_name='Port')),
                ('user', models.CharField(blank=True, max_length=32, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z_@\\-\\.]*$', 'Special char not allowed')], verbose_name='User')),
                ('password', common.fields.model.EncryptCharField(blank=True, max_length=256, null=True, verbose_name='Password')),
                ('database', models.CharField(blank=True, max_length=128, null=True, verbose_name='Database')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('created_by', models.CharField(max_length=128, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
            ],
            options={
                'verbose_name': 'Database',
                'ordering': ('name',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='database',
            unique_together={('org_id', 'name')},
        ),
    ]
