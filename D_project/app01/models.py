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
