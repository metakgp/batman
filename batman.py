from functools import partial
import json
import sys

from slackclient import SlackClient
import redis

token = 'xoxb-11032520071-yPycTGRY3ZmAaQMZEWCN6Wwf'
sc = SlackClient(token)

slack = partial(sc.api_call, username='batman', link_names=1, icon_url='http://i.picresize.com/images/2015/09/20/tdpsU.jpg')

redis_client = redis.StrictRedis()

while True:
    message = redis_client.brpop('slack:recent-changes')
    print message[1]
    try:
        data = json.loads(message[1])
	print data['text']
	print slack('chat.postMessage', text=data['text'],
                 channel='#recent-changes')
    except ValueError as e:
        print "Got the following error : "
	print e
	pass
slack('chat.postMessage' ,text='@hargup , @icyflame , @athityakumar , @defcon , @xtinct , @nishnik , @ghostwriternr I am dead please throw me back in the Lazrus pit ASAP ! ', channel='#meta-x')
