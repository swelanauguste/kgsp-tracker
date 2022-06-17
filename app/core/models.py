import uuid

from click import edit
from django.db import models
from django.urls import reverse
from users.models import User


class Ticket(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ticket_created_by", default=1
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ticket_updated_by", default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    uid = models.URLField(default=uuid.uuid4, editable=False, unique=True)
    summary = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ticket_assigned_to",
        blank=True,
        null=True,
        default=1,
    )

    def get_absolute_url(self):
        return reverse("ticket-detail", kwargs={"pk": self.id})

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
    uid = models.URLField(default=uuid.uuid4, editable=False, unique=True)
    note = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.ticket.summary} - {self.note}"
