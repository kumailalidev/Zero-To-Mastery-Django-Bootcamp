from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
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
