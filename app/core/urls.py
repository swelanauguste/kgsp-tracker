from django.urls import path

from . import views

urlpatterns = [
    path("", views.TicketListView.as_view(), name="ticket-list"),
    path("detail/<slug:pk>/", views.TicketDetailView.as_view(), name="ticket-detail"),
    path("ticket-create/", views.TicketCreateView.as_view(), name="ticket-create"),
]
