from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm


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
    context = {'topic': selected_topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Create a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Display a blank of invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
