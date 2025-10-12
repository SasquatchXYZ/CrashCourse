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


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    selected_topic = Topic.objects.get(id=topic_id)
    entries = selected_topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
