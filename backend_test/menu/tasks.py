# slack
import slack
import slack.chat

# models
from backend_test.staff.models import Order

from django.conf import settings
from django.template.loader import get_template
from django.template import Context

from celery import shared_task
from datetime import datetime

@shared_task()
def send_slack_message():
	actual_date = datetime.now()
	print(actual_date)
	orders = Order.objects.filter(menu__date=actual_date.date(), product=None)
	slack.api_token = settings.SLACK_TOKEN
	template = get_template('slack/order_message.slack')
	for order in orders:
		context = {
			"order": order
		}
		html_content = template.render(context)
		slack.chat.post_message('@alejandro-243', html_content, username='Almuerzo')
	return 'Done'