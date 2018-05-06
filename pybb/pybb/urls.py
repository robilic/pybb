"""pybb URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

import board.views

urlpatterns = [
    url(r'^viewforum/(?P<forum_id>\d+)/', board.views.view_forum, name='viewforum'),
    url(r'^viewtopic/(?P<topic_id>\d+)/', board.views.view_topic, name='viewtopic'),
    url(r'^(?P<forum_id>\d+)/new_post/', board.views.new_post, name='new_post'),

    url(r'^(?P<forum_id>\d+)/submit_new_post/', board.views.submit_new_post, name='submit_new_post'),
    url(r'^submit_new_reply/(?P<topic_id>\d+)/', board.views.submit_new_reply, name='submit_new_reply'),

    url(r'^messages/$', board.views.messages, name='messages'),
    url(r'^messages/new', board.views.messages_new, name='messages_new'),
    url(r'^messages_view/(?P<message_id>\d+)', board.views.messages_view, name='messages_view'),
    url(r'^submit_message/$', board.views.submit_message, name='submit_message'),
    url(r'^submit_message/(?P<message_id>\d+)', board.views.submit_message, name='submit_message'),
    url(r'^index/', board.views.index, name='index'),
    url(r'^faq/', board.views.faq, name='faq'),
    url(r'^profile/(?P<user_id>\d+)/', board.views.profile, name='profile'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
]
