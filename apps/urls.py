from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>', views.post_results, name='index2'),
    path('results/', views.result_list, name='index3'),
    path('results/<int:pk>', views.view_detail, name='result-detail'),
    url('^$', views.runner_check, name='check'),
    path('testcase/index/', views.get_index, name='index'),
    path('testcase/new/', views.post_new, name='new'),
    path('testcase/edit/<id>/', views.post_edit, name='edit'),
    path('testcase/show/<id>/', views.detail, name='detail'),
    path('testcase/delete/<id>/', views.delete, name='delete')

]
