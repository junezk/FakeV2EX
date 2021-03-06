# Generated by Django 2.0.2 on 2018-03-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20180308_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='所在城市'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=11, null=True, verbose_name='电话'),
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]
