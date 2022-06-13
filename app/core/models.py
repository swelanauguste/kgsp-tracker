import uuid

from click import edit
from django.db import models
from users.models import User


class Ticket(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ticket_created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ticket_updated_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    id = models.URLField(
        default=uuid.uuid4, editable=False, primary_key=True, unique=True
    )
    summary = models.CharField(max_length=100)
    details = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.summary


class Note(models.Model):
    ticket = models.ForeignKey(
        Ticket, related_name="comments", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_updated_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    id = models.URLField(
        default=uuid.uuid4, editable=False, primary_key=True, unique=True
    )
    note = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.ticket.summary} - {self.note}"
