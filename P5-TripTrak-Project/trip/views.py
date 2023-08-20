from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Trip, Note


class HomeView(TemplateView):
    template_name = "trip/index.html"


def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        "trips": trips,
    }
    return render(request, "trip/trip_list.html", context)


class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy("trip-list")
    fields = ["city", "country", "start_date", "end_date"]
    # template => model_form.html : trip_form.html

    def form_valid(self, form):
        # adding owner field and setting value a logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TripDetailView(DetailView):
    model = Trip
    # template => model_detail.html : trip_detail.html

    # Updating context variable so that it also have Notes model information
    # Overriding default behavior get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context["object"]
        notes = trip.notes.all()
        context["notes"] = notes
        return context


class NoteDetailView(DetailView):
    model = Note
    # template => model_detail.html : note_detail.html


class NoteListView(ListView):
    model = Note
    # template => model_list.html : note_list.html

    # Filtering queryset
    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset


class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy("note-list")
    fields = "__all__"
    # template => model_form.html : note_form.html

    # Overriding get_form to avoid creating note for all trips present in database
    # Only logged in user trips should be visible
    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields["trip"].queryset = trips
        return form


class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy("note-list")
    fields = "__all__"
    # template => model_form.html : note_form.html; Uses same template for creating note

    # Overriding get_form to avoid updating note for all trips present in database
    # Only logged in user trips should be visible
    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields["trip"].queryset = trips
        return form


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("note-list")
    # No template needed - Send a POST request to this url.


class TripUpdateView(UpdateView):
    model = Trip
    success_url = reverse_lazy("trip-list")
    fields = ["city", "country", "start_date", "end_date"]
    # template => model_form.html : trip_form.html


class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy("trip-list")
