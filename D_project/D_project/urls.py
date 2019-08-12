"""D_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^login_tr/$', views.login_tr),
    #------------添加一个数据库表------------#
    url(r'^list_book/$',views.list_book),
    #------------对于已有数据进行添加--------#
    url(r'^list_add/$',views.list_add),
    #------------对已有数据进行删除----------#
    url(r'^list_del/$',views.list_del),
    #------------对当前已有数据进行修改------#
    url(r'^list_edit/$',views.list_edit),
]
