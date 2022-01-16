from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import slack
import slack.chat
from django.conf import settings

def test_slack_message(request, *args, **kwargs):
    slack.api_token = settings.SLACK_TOKEN
    slack.chat.post_message('@alejandro-243', 'Hello slackers!', username='mybot')

    return JsonResponse({
        "hola": "as"
    })
