from django.shortcuts import render

from .models import Topic


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    ordered_topics = Topic.objects.order_by('date_added')
    context = {'topics': ordered_topics}
    return render(request, 'learning_logs/topics.html', context)
