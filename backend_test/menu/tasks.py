from datetime import datetime

from celery import shared_task
from django.conf import settings
from django.template import Context
from django.template.loader import get_template

import slack
import slack.chat

from backend_test.staff.models import Order


@shared_task()
def send_slack_message():
    actual_date = datetime.now()
    orders = Order.objects.filter(menu__date=actual_date.date(), product=None)
    slack.api_token = settings.SLACK_TOKEN
    template = get_template("slack/order_message.slack")
    message_send = 0
    for order in orders:
        context = {"order": order}
        html_content = template.render(context)
        slack.chat.post_message("@alejandro-243", html_content, username="Almuerzo")
        message_send += 1
    return message_send
