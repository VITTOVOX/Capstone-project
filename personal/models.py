"""Database models for the polls/blog application."""

from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


class Post(models.Model):
    """Blog/general post with title, body, timestamps and type."""

    POST_TYPES = [
        ('post', 'Post'),
        ('blog', 'Blog Post'),
    ]

    title = models.CharField(
        max_length=200,
        help_text="Enter the post title",
        verbose_name="Title"
    )
    body = models.TextField(
        help_text="Content of the post",
        verbose_name="Body"
    )
    signature = models.CharField(
        max_length=100,
        blank=True, null=True,
        help_text="Optional author signature",
        verbose_name="Signature"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        help_text="Date the post was created",
        verbose_name="Created Date"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        help_text="Date the post was last updated"
    )
    post_type = models.CharField(
        max_length=10,
        choices=POST_TYPES,
        default='post',
        help_text="Type of the post",
        verbose_name="Post Type"
    )

    def __str__(self) -> str:
        """Return the post's title."""
        return self.title

    def get_absolute_url(self) -> str:
        """Return the canonical URL for this post."""
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-date']
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Question(models.Model):
    """Poll question with publish and update timestamps."""

    question_text = models.CharField(
        max_length=200,
        help_text="Enter the question text",
        verbose_name="Question Text"
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        help_text="Date the question was published",
        verbose_name="Published Date"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date the question was last updated",
        verbose_name="Last Updated"
    )

    def __str__(self) -> str:
        """Return the question text."""
        return self.question_text

    def get_absolute_url(self) -> str:
        """Return the canonical URL for this question."""
        return reverse('question_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Choice(models.Model):
    """Selectable option linked to a Question with a vote counter."""

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices',
        verbose_name="Question"
    )
    choice_text = models.CharField(
        max_length=100,
        help_text="Text for the choice",
        verbose_name="Choice Text"
    )
    votes = models.IntegerField(
        default=0,
        help_text="Number of votes for this choice",
        verbose_name="Votes"
    )

    def __str__(self) -> str:
        """Return the choice text."""
        return self.choice_text

    def clean(self) -> None:
        """Ensure votes cannot be negative."""
        if self.votes < 0:
            raise ValidationError({'votes': "Votes cannot be negative."})

    def save(self, *args, **kwargs) -> None:
        """Validate the model before saving to the database."""
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"