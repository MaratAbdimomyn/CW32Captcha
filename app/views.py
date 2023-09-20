from unicodedata import category
from django.views.generic import CreateView, ListView
from django.shortcuts import render
from .forms import *
from .models import *

class ListPlanet(ListView):
    model = Planets
    template_name = 'home.html'
    context_object_name = 'item'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = SearchForm(request.POST)

        if form.is_valid():
            run = form.cleaned_data['run']
            self.object_list = Planets.objects.filter(name__icontains=run)
            context = self.get_context_data()
            return self.render_to_response(context)
        return render(request, self.template_name, {'search_form':form, 'items': self.object_list})

class CreatePlanet(CreateView):
    form_class = ItemForm
    template_name = 'create.html'
    success_url = '/'