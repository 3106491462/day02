from django.urls import re_path
from helloworld import views

urlpatterns = [
    # 通过re_path方法添加URL配置项，指定访问地址和视图函数之间的对应关系
    # 配置格式：re_path('URL地址', '视图函数')
    re_path(r'^hello-world/$', views.first_view_func),
]