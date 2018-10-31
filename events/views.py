from django.shortcuts import render
from . import models
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import AddEventForm, AddEventTimeForm
from datetime import timedelta


class EventsUpcomingListView(LoginRequiredMixin, generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        queryset = models.Event.objects.filter(
            eventtimes__start_time__gte=timezone.now(),
            User=self.request.user
        )
        return queryset


class EventsInOneDayListView(LoginRequiredMixin, generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        queryset = models.Event.objects.filter(
            eventtimes__start_time__gte=timezone.now(),
            eventtimes__start_time__lte=timezone.now() + timedelta(days=1),
            User=self.request.user
        )
        return queryset


class EventsInOneYearListView(LoginRequiredMixin, generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        queryset = models.Event.objects.filter(
            eventtimes__start_time__gte=timezone.now(),
            eventtimes__start_time__lte=timezone.now() + timedelta(days=365),
            User=self.request.user
        )
        return queryset


class EventsInOneMonthListView(LoginRequiredMixin, generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        queryset = models.Event.objects.filter(
            eventtimes__start_time__gte=timezone.now(),
            eventtimes__start_time__lte=timezone.now() + timedelta(days=31),
            User=self.request.user
        )
        return queryset


class EventDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Event
    template_name = 'events/event_detail.html'
    context_object_name = 'object'

    def get_queryset(self):
        queryset = super(EventDetailView, self).get_queryset().filter(
            User=self.request.user)
        return queryset


@login_required
def event_add(request):
    message = ""
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        formTime = AddEventTimeForm(request.POST)
        if form.is_valid() and formTime.is_valid():
            event_ob = form.save(commit=False)
            event_ob.User = request.user
            event_ob.save()
            form.save_m2m()

            time_ob = formTime.save(commit=False)
            time_ob.event = event_ob
            time_ob.start_time = formTime.cleaned_data["start_time"]
            time_ob.save()

            form = AddEventForm()
            formTime = AddEventTimeForm()
            message = "Inserted successfully"
    else:
        form = AddEventForm()
        formTime = AddEventTimeForm()
    return render(request, "events/event_add.html",
                  {'form': form, 'formTime': formTime, 'message': message})
