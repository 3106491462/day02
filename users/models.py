from django.db import models
class User(models.Model):
    """用户模型类"""
    # verbose_name：对字段的解析说明，相当于注释的作用
    # max_length：指定字符串内容的最大长度为多少个字符
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    # default：设置向数据库添加数据时，字段使用的默认值
    gender = models.BooleanField(default=False, verbose_name='性别')
    age = models.IntegerField(default=18, verbose_name='年龄')
    # null=True：生成数据表时，数据表的对应字段允许为NULL
    mobile = models.CharField(max_length=11, null=True, verbose_name='手机号')

    class Meta:
        # 指定迁移时生成的数据表的名称
        db_table = 'tb_users'
        # 模型类的解析说明，相当于注释的作用
        verbose_name = '用户表'
# Create your models here.
