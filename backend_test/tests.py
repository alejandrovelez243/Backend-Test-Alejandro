from django.test import TestCase

from backend_test.celery import app
from backend_test.envtools import getenv


class SettingsTest(TestCase):
    def test_getenv(self):
        env = getenv("APP_LOGGING_LEVEL", default=True)
        self.assertEqual(env, "INFO")

    def test_getenv_fail(self):
        env = getenv("FAIL", default=True)
        self.assertEqual(env, True)

    def test_celery(self):
        self.assertIsNotNone(app)
