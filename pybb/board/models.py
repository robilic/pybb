from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class PostIcon(models.Model):
	filename = models.CharField(max_length=128)

	def __str__(self):
		return '%s' % (self.filename)

class Forum(models.Model):
	name = models.CharField(max_length=80)
	description = models.CharField(max_length=256)
	last_post_created = models.DateTimeField(null=True)
	last_post_author = models.ForeignKey(User,null=True,related_name='+')
	#last_post_thread = models.OneToOneField(Post,null=True)
	topics_count = models.IntegerField(default=0)
	posts_count = models.IntegerField(default=0)

	def __str__(self):
		return '%s' % (self.name)

class Topic(models.Model):
	forum = models.ForeignKey(Forum)
	title = models.CharField(max_length=80)
	created = models.DateTimeField(null=True)
	last_post_created = models.DateTimeField(null=True)
	last_post_author = models.ForeignKey(User,null=True,related_name='+')
	author = models.ForeignKey(User)
	reply_count = models.IntegerField(default=0)
	view_count = models.IntegerField(default=0)
	post_icon = models.ForeignKey(PostIcon,null=True)
	# sticky/mod/locked
	# should this update the forum it is linked to?
	def __str__(self):
		return '%s' % (self.title)

class Post(models.Model):
	body    = models.TextField(max_length=10000)
	created = models.DateTimeField()
	topic   = models.ForeignKey(Topic)
	author  = models.ForeignKey(User, null=True)
	# Deleted, edited, etc

	def save(self, *args, **kwargs):
		# update the topic this is linked to
		t = Topic.objects.get(pk=self.topic_id)
		t.last_post_author = self.author
		t.last_post_created = self.created
		t.reply_count = Post.objects.filter(topic_id = self.topic_id).count()
		t.save()
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return 'topic: %d, %s' % (self.topic.id, self.body)

class PrivateMessage(models.Model):
	body      = models.TextField(max_length=10000)
	subject   = models.CharField(max_length=80)
	author    = models.ForeignKey(User, null=True, related_name='+')
	recipient = models.ForeignKey(User, null=True, related_name='+')
	created   = models.DateTimeField()
	post_icon = models.ForeignKey(PostIcon, null=True)
	viewed    = models.BooleanField()

	def __str__(self):
		return '%s' % (self.subject)

class Profile(models.Model):
	user         = models.OneToOneField(User, on_delete=models.CASCADE)
	created      = models.DateField(null=True, blank=True)
	location     = models.CharField(max_length=30, blank=True)
	custom_title = models.CharField(max_length=30, blank=True)
	post_count   = models.IntegerField(default=0)

	def __str__(self):
		return '%s' % (self.user.get_username())

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

