from django.conf.urls import url
from apps import views

urlpatterns = [
    url('^$', views.runner_check, name='check'),
]
