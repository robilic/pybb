from django.contrib import admin

from board.models import Topic, Post, Profile, Forum, PrivateMessage
# Register your models here.
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Forum)
admin.site.register(PrivateMessage)
