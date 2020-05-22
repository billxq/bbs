"""my_bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from post import views

urlpatterns = [
    path('hello/', views.hello_django_bbs),
    path('topic_list/', views.topic_list_view),
    url(r'topic/(?P<topic_id>\d+)/', views.topic_detail_view),
    path('topic_comment/', views.add_comment_to_topic_view),
]
