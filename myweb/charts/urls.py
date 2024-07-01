from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.chart_view, name='chart-view'),
    # 这里的 'chart/' 是路径，views.chart_view 是处理该路径请求的视图函数
]
