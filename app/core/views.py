from django.views.generic import CreateView, DetailView, ListView

from .models import Note, Ticket


class TicketListView(ListView):
    paginate_by = 25
    model = Ticket
    
    
class TicketDetailView(DetailView):
    model = Ticket
    
    
class TicketCreateView(CreateView):
    model = Ticket
