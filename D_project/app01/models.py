from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key = True)  # 创建一个自增的ID列作为主键
    email = models.CharField(max_length = 32) # -->varchar(32)
    pwd = models.CharField(max_length = 32)  # --> varchar(32)


class Publisher(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 32)
    def __str__(self):
        return self.name

class Author(models.Model):
    id = models.AutoField(primary_key = True)#还是要创建主键
    title = models.CharField(max_length = 32)#图书名
    #在Django 1.11中默认就是联级删除，Django 2.0及以上版本必须指定on_delete
    publisher = models.ForeignKey(to = 'Publisher',on_delete = models.CASCADE)#这是一个外键