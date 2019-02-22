# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-30 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_auto_20180607_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('source', models.CharField(default='', max_length=32, verbose_name='公司标识')),
                ('password', models.CharField(max_length=128, verbose_name='登录密码')),
                ('corp_id', models.CharField(max_length=32, unique=True, verbose_name='第三方公司ID')),
                ('corp_secret', models.CharField(max_length=32, verbose_name='管理组的凭证密钥')),
                ('ip_list', models.CharField(max_length=256, verbose_name='服务器ip百名单')),
                ('domain', models.CharField(default='', max_length=32, verbose_name='服务器域名')),
                ('token', models.CharField(max_length=32, verbose_name='令牌')),
                ('status', models.SmallIntegerField(default=1, verbose_name='状态：-1, 不可用, 0 待审核，1可用')),
            ],
            options={
                'verbose_name_plural': '入驻公司',
                'verbose_name': '入驻公司',
            },
        ),
    ]
