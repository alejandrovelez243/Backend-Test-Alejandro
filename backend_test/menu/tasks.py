# Flask
import slack
import slack.chat

from django.conf import settings
from celery import task

@task()
def send_slack_message(order=1):
	print("ENTRE")
	slack.api_token = settings.SLACK_TOKEN
	slack.chat.post_message('@alejandro-243', 'Hello slackers!', username='mybot')
	return None