# Generated by Django 3.0 on 2023-11-19 17:49

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcd1234567', length=10, max_length=20, prefix='cat', unique=True),
        ),
    ]
