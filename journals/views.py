from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# methods
def check_topic_owner(request, owner):
	"""Check if the current user is the topic owner and raise 404 if not."""
	if request.user != owner:
		raise Http404


# Create your views here.
def index(request):
	"""The home page for journals."""
	return render(request, 'journals/index.html')


def info(request):
	"""The info page"""
	return render(request, 'journals/info.html')


@login_required
def topics(request):
	"""The topics page."""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics':topics}
	return render(request, 'journals/topics.html', context)


@login_required
def topic(request, topic_id):
	"""Show a single topic and all its entries."""

	# DB QUERY
	topic = Topic.objects.get(id=topic_id)
	
	# Raise 404 if user tries to access other user's topic
	check_topic_owner(request, topic.owner)

	# DB QUERY
	# use entry with _set to get all the objects associated 
	# to this topic via foreign key entry
	entries = topic.entry_set.order_by('date_added')
	
	context = {'topic':topic, 'entries':entries}
	return render(request, 'journals/topic.html', context)


@login_required
def new_topic(request):
	"""Form to add new topic."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = TopicForm()
	else:
		# POST data submitted; process data.
		# request.POST stores the data entered by the user
		form = TopicForm(data = request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.owner = request.user
			form.save()
			# redirect back to the topics page after submitted topic
			# reverse() function gets URL from a URL name pattern or a view
			return HttpResponseRedirect(reverse('journals:topics'))

	context = {'form': form}
	return render(request, 'journals/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
	"""Form to add a new entry for a particular topic."""
	topic = Topic.objects.get(id=topic_id)

	check_topic_owner(request, topic.owner)

	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data = request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			form.save()
			return HttpResponseRedirect(
				reverse('journals:topic', args=[topic_id]))

	context = {'topic':topic, 'form': form}
	return render(request, 'journals/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
	"""Edit an existing entry."""
	entry = Entry.objects.get(id = entry_id)
	topic = entry.topic

	check_topic_owner(request, topic.owner)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry
		form = EntryForm(instance = entry)
	else:
		# POST data submitted; process data.
		form = EntryForm(
			instance = entry,
			data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(
				reverse('journals:topic', args=[topic.id]))

	context = {'entry':entry, 'topic':topic, 'form': form}
	return render(request, 'journals/edit_entry.html', context)

