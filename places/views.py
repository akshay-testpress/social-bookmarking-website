from django.shortcuts import render
from .forms import PlaceForm
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required()
def insert_places(request):
    message = ""
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form.save_m2m()
            form = PlaceForm()
            message = "Inserted successfuly"
    else:
        form = PlaceForm()
    return render(request, "places/insertplace.html",
                  {'form': form, 'message': message})


class PlaceView(LoginRequiredMixin, generic.ListView):
    template_name = 'places/place_list.html'
    context_object_name = 'objects'
    queryset = models.Place.objects.order_by('title')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Places"
        context['page_heading'] = "Places"
        return context


class PlaceDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Place
    template_name = 'places/place_detail.html'
    context_object_name = 'object'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Place"
        return context
