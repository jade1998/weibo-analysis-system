# Generated by Django 2.1.7 on 2019-04-09 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpiderAPI', '0004_auto_20190401_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentInfo',
            fields=[
                ('c_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='评论的ID')),
                ('c_created_at', models.DateTimeField(blank=True, verbose_name='评论创建时间')),
                ('c_source', models.TextField(blank=True, verbose_name='评论的来源')),
                ('c_text', models.TextField(blank=True, verbose_name='评论的内容')),
                ('c_like_num', models.IntegerField(blank=True, default=0, verbose_name='评论点赞数')),
                ('c_userId', models.CharField(blank=True, max_length=50, verbose_name='评论用户的微博ID')),
                ('c_user_name', models.CharField(blank=True, max_length=300, verbose_name='评论用户的微博昵称')),
                ('C_profile_image_url', models.TextField(blank=True, verbose_name='评论用户的头像')),
                ('C_profile_url', models.TextField(blank=True, verbose_name='评论用户的主页')),
            ],
            options={
                'verbose_name': '评论详情',
                'verbose_name_plural': '评论详情',
            },
        ),
        migrations.CreateModel(
            name='CommentWeiboInfo',
            fields=[
                ('wb_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='微博的ID')),
                ('wb_userId', models.CharField(max_length=50, verbose_name='微博用户的ID')),
                ('wb_userName', models.CharField(max_length=50, verbose_name='微博用户的昵称')),
                ('wb_user_profile_image_url', models.TextField(verbose_name='微博用户的头像')),
                ('wb_created_at', models.DateTimeField(blank=True, verbose_name='微博创建时间')),
                ('wb_source', models.TextField(blank=True, verbose_name='微博来源')),
                ('wb_text', models.TextField(verbose_name='微博内容')),
                ('wb_pic_ids', models.TextField(blank=True, verbose_name='微博图片')),
                ('wb_reposts', models.IntegerField(blank=True, default=0, verbose_name='转载数')),
                ('wb_comments', models.IntegerField(blank=True, default=0, verbose_name='评论数')),
            ],
            options={
                'verbose_name': '微博评论',
                'verbose_name_plural': '微博评论',
            },
        ),
        migrations.AddField(
            model_name='commentinfo',
            name='CommentWeiboInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpiderAPI.CommentWeiboInfo', verbose_name='微博用户信息'),
        ),
    ]