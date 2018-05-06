from board.models import Topic, Post, Profile, Forum, PostIcon
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone

class FakeUser:
	def __init__(self, name, pw, location, custom_title):
		u = User.objects.create_user(name, password=pw)
		u.profile.created = datetime.today()
		u.profile.custom_title = custom_title
		u.profile.location = location
		u.save()

class ExampleForum:
	def __init__(self, name, description):
		f = Forum()
		f.name = name
		f.descrption = description
		f.save()

class ExampleTopic:
	def __init__(self, forum, title, author, created, post_icon):
		t = Topic()
		t.forum_id= forum
		t.title = title
		t.author_id = author
		t.created = created
		t.post_icon_id = post_icon
		t.save()

class ExamplePost:
	def __init__(self, body, created, topic, author):
		p = Post()
		p.body = body
		p.created = created
		p.topic_id = topic
		p.author_id = author
		p.save()

class DefaultIcon:
	def __init__(self, filename):
		p = PostIcon()
		p.filename = filename
		p.save()

FakeUser('SarahConnor', 'topsecret', 'Tuscadero Mental Hospital', '')
FakeUser('JohnConnor', 'topsecret', 'The Mall', 'Leader of the Resistance')
FakeUser('T800', 'topsecret', 'Biker Bar', 'Original Terminator')
FakeUser('T1000', 'topsecret', '', 'Polymetic Alloy')
FakeUser('Arnold', 'topsecret', '', 'Hasta La Vista Baby')
FakeUser('MilesDyson', 'topsecret', 'Cyberdyne Systems', 'Lead CPU Designer')
FakeUser('Skynet', 'topsecret', 'Judgement Day', 'Self-Aware')

DefaultIcon('info.gif')
DefaultIcon('question.gif')
DefaultIcon('alert.gif')
DefaultIcon('star.gif')
DefaultIcon('thinking.gif')
DefaultIcon('fire.gif')
DefaultIcon('heart.gif')
DefaultIcon('radioactive.gif')

ExampleForum('The Chit Chat Lounge', 'General forum for discussion and chat. Keep it civil.')
ExampleForum('The Sports Page', 'Talk about your favorite sports, from football to hockey')
ExampleForum('Tech Zone', 'Computers, phones, and gadgets')

ExampleTopic(1, 'Who still watches SNL?', 2, timezone.now() - timedelta(hours=27), 1)
ExampleTopic(1, 'Trucks: RAM, Ford, or Chevy?', 3, timezone.now() - timedelta(hours=26), 2)
ExampleTopic(1, 'Black Friday Deals Thread', 4, timezone.now() - timedelta(hours=25), 3)

ExamplePost('I never watch it anymore. I quit back in 2005 when that one funny guy left the show.', 
	timezone.now() - timedelta(hours=20), 1, 3)
ExamplePost('I still watch it all the time. Very funny!',
	timezone.now() - timedelta(hours=19), 1, 2)
ExamplePost('Maybe. Only if nothing else is on...', 
	timezone.now() - timedelta(hours=18), 1, 4)

ExamplePost('The new Ford F150 has a 10 speed transmission and it also has the new\n400hp 3.5 EcoBoost V6. Hard to beat that.',
	timezone.now() - timedelta(hours=19), 2, 5)
ExamplePost('The Dodge Ram is also all new for 2018',
	timezone.now() - timedelta(hours=18), 2, 3)
ExamplePost("""What would a new Ford Super Duty Raptor look like? The guys at Defco Trucks in Colorado think it would be like this BA-350 Stage-2 Ford F-350 with a fully built suspension, body, and 43-inch tall tires. BA-350 stands for Bad Ass, which is a crew cab heavy duty truck that is 7-2 tall and 93 inches wide.
The stage-2 is using a unique suspension design front and rear to provide up to 12 inches of travel in the front and 17 inches in the back. It’s rolling on 43-inch tires that are also original equipment on the Mercedes Unimog trucks. The suspension uses specific springs and King shocks with a cantilever design in the rear.

The widebody fenders front and rear are made out of fiberglass and look to be well integrated into the overall look, including paint.

The 6.7L Power Stroke V8 is left in stock form including all of the emissions equipment (DEF is still there), but the rear section of the exhaust had to be modified to accommodate for the special suspension.

The truck you see here is still equipped with a 3.55 rear axle gear ratio (the guys are working on a 4.30 gearing option), but this truck still has plenty get up and go as we found out on a short ride. The knobby tires make a distinct and noticeable hum at highway speeds, as you would expect. This nearly 9,500 lbs truck gets 12-13 MPG in the city and about 17 MPG on the highway, according to Doug.

There are three stages for this turn-key conversion.

The stage-1 includes the widebody fenders, bumpers, tires, and the whole look of the BA-350 truck – but without the fancy high-travel suspension. This is priced at $38,850 on top of the price of a donor 2017 and up Super Duty truck.

Stage-2 or basically the truck you see here is priced at $69,000 plus the price of the truck.

There is another Stage that the company calls LTFO (or limitless) that adds a roll cage, spare tire carriers, engine tune, and more for additional $25,000+.""",
	timezone.now() - timedelta(hours=17), 2, 4)

ExamplePost('Any good deals on snowblowers? Looking for at least 10% off.',
	timezone.now() - timedelta(hours=18), 3, 5)
ExamplePost('MacBooks are $200 off at B&H Photo',
	timezone.now() - timedelta(hours=18), 3, 4)
ExamplePost("Kroger has Lowe's gift cards, $125 for $100",
	timezone.now() - timedelta(hours=18), 3, 2)


ExampleTopic(2, 'Who is going to win the superbowl?', 5, timezone.now() - timedelta(hours=21), 4)

ExamplePost('My money is on Tom Brady and the New England Patriots!', 
	timezone.now() - timedelta(hours=20), 4, 3)
ExamplePost('The NFL is rigged. They already have it decided.',
	timezone.now() - timedelta(hours=19), 4, 2)
ExamplePost('Anyone selling football board squares?', 
	timezone.now() - timedelta(hours=18), 4, 4)


ExampleTopic(2, 'Who still watches soccer', 7, timezone.now() - timedelta(hours=23), 5)

ExamplePost('I never watch it anymore. I quit back in 2005 when that one funny guy left the show.', 
	timezone.now() - timedelta(hours=20), 5, 2)
ExamplePost('I still watch it all the time. Very funny!',
	timezone.now() - timedelta(hours=19), 5, 5)
ExamplePost('Maybe. Only if nothing else is on...', 
	timezone.now() - timedelta(hours=18), 5, 4)


ExampleTopic(3, 'My new MacBook Pro keyboard broke', 2, timezone.now() - timedelta(hours=27), 6)

ExamplePost('What a piece of crap. I just got back from the Apple store', 
	timezone.now() - timedelta(hours=20), 6, 3)
ExamplePost('Did they repair or replace it?',
	timezone.now() - timedelta(hours=19), 6, 2)
ExamplePost('Screw Apple I bought a Dell XPS 13', 
	timezone.now() - timedelta(hours=18), 6, 4)

