from django.test import TestCase

# Create your tests here.
from datetime import datetime, timedelta
from django.utils import timezone

from polls.models import Question


class QuestionModelTest(TestCase):
    def test_was_published_recently(self):
        time = timezone.now() + timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)