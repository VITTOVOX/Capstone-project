"""Test suite for the polls/blog application.

This module contains unit tests for models, views, and other
functionality within the application.
"""

from django.test import TestCase
from .models import Question


class QuestionModelTests(TestCase):
    """Tests for the Question model."""

    def test_str_returns_question_text(self):
        """__str__() should return the question text."""
        question = Question(question_text="Is this a test?")
        self.assertEqual(str(question), "Is this a test?")

    def test_default_votes_is_zero(self):
        """Newly created questions should have zero votes by default."""
        question = Question(question_text="Another test?")
        # assumes you have a related Choice model with default votes=0
        # Here you'd test your model logic, e.g., choices, default values
        self.assertEqual(question.choice_set.count(), 0)
