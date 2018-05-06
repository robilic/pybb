from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User

import datetime

from .models import Topic, Post, Profile, Forum, PostIcon, PrivateMessage

# view forum
def view_forum(request, forum_id):
	topic_list = Topic.objects.filter(forum=forum_id).order_by('created')
	forum = Forum.objects.get(pk=forum_id)

	context = { 'topic_list': topic_list,
				'forum': forum, }
	return render(request, 'board/viewforum.html', context)

def index(request):
	forum_list = Forum.objects.order_by('id')
	context = { 'forum_list': forum_list, }
	return render(request, 'board/index.html', context)

def view_topic(request, topic_id):
	topic_post_list = Post.objects.filter(topic=topic_id).order_by('created')
	topic = Topic.objects.get(pk=topic_id)
	context = { 'topic_post_list': topic_post_list, 
				'topic': topic,}
	topic.view_count = topic.view_count + 1
	topic.save()
	return render(request, 'board/viewtopic.html', context)

def profile(request, user_id):
	user = User.objects.get(pk=user_id)
	profile = Profile.objects.get(pk=user_id)
	context = { 'user': user,
				'profile': profile }

	return render(request, 'board/profile.html', context)

def faq(request):
	context = { }
	return render(request, 'board/faq.html', context)

def messages(request):
	posticons = PostIcon.objects.all()
	private_message_list = PrivateMessage.objects.filter(recipient=request.user.id).order_by('created')
	context = { 'posticons': posticons,
				'private_message_list': private_message_list }
	return render(request, 'board/messages_index.html', context)

def messages_new(request):
	posticons = PostIcon.objects.all()
	context = { 'posticons': posticons }
	return render(request, 'board/messages_new.html', context)

def messages_view(request, message_id):
	post_icons = PostIcon.objects.all()
	private_message = PrivateMessage.objects.get(pk=message_id)
	context = { 'post_icons': post_icons, 'private_message':private_message }
	return render(request, 'board/messages_view.html', context)

def submit_message(request, message_id='none'):
	if message_id == 'none':
		pm = PrivateMessage()
		pm.author       = request.user
		pm.recipient    = User.objects.get(username=request.POST['recipient'])
		pm.subject      = request.POST['subject']
		pm.body         = request.POST['body']
		pm.post_icon_id = request.POST['post_icon']
		pm.created      = datetime.datetime.now()
		pm.viewed       = False
		pm.save()
	else:
		pm = PrivateMessage()
		om = PrivateMessage.objects.get(pk=message_id)
		pm.author = om.recipient
		pm.recipient = om.author
		
		if om.subject[0:3] != 'Re:':
			pm.subject = "Re: " + om.subject
		else:
			pm.subject = om.subject		

		pm.body = request.POST['body']
		pm.post_icon = om.post_icon
		pm.created = datetime.datetime.now()
		pm.viewed = False
		pm.save()

	posticons = PostIcon.objects.all()
	context = { 'posticons': posticons }
	return HttpResponseRedirect(reverse('messages'))

def new_post(request, forum_id):
	forum = Forum.objects.get(pk=forum_id)
	posticons = PostIcon.objects.all()
	context = { 'posticons': posticons,
				'forum': forum, }
	return render(request, 'board/new_post.html', context)

def submit_new_post(request, forum_id):
	new_topic = Topic()
	new_topic.author = request.user
	new_topic.title = request.POST['topic_title']
	new_topic.post_icon_id = request.POST['post_icon']
	new_topic.forum_id = forum_id
	new_topic.created = datetime.datetime.now()
	new_topic.save()
	
	new_post = Post()
	new_post.author = new_topic.author
	new_post.body = request.POST['post_body']
	new_post.created = new_topic.created
	new_post.topic_id = new_topic.id
	new_post.save()

	new_topic.last_post_created = new_topic.created
	new_topic.last_post_author_id = new_topic.author
	new_topic.save()
	return HttpResponseRedirect(reverse('viewtopic', args=(new_topic.id,)))

def submit_new_reply(request, topic_id):
	new_post = Post()
	new_post.author = request.user
	new_post.body = request.POST['post_body']
	new_post.created = datetime.datetime.now()
	new_post.topic_id = topic_id
	new_post.save()
	topic = Topic.objects.get(pk=topic_id)
	topic.reply_count = topic.reply_count + 1
	topic.last_post_created = new_post.created
	topic.last_post_author = new_post.author
	topic.save()
	return HttpResponseRedirect(reverse('viewtopic', args=(topic_id,)))

