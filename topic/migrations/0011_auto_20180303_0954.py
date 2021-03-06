# Generated by Django 2.0.2 on 2018-03-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0010_auto_20180302_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='html_content',
            field=models.TextField(blank=True, max_length=20000, null=True, verbose_name='Topic html content'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=models.TextField(max_length=20000, verbose_name='Topic content'),
        ),
    ]
