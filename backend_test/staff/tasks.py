from backend_test.celery import app
# Flask
import slack
import slack.chat

@app.task
def send_slack_message(message, people):
    print("ENTRE")


def test_slack_message(request, *args, **kwargs):
	slack.api_token = settings.SLACK_TOKEN
	slack.chat.post_message('@alejandro-243', 'Hello slackers!', username='mybot')

	return JsonResponse({
		"hola": "as"
	})