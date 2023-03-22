from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Project
# from django.db.models import  When, Case, Value
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
# Genericview

class CreateProject(CreateView):
    model = Project
    # fields = ['title', 'description', 'estimated_hours', 'start_date', 'end_date']
    fields = "__all__"
    # print("THis")
    template_name = 'todo/create.html'
    success_url = '/todo/list'

    # def form_valid(self,form):
    #     print("valid")

@method_decorator(login_required, name='dispatch')
class ListAllProject(ListView):
    model = Project
    paginate_by = 50
    template_name = 'todo/list.html'
    context_object_name = 'projects'
    ordering = ['-title']

    def get_queryset(self):   # for queries
        return Project.objects.order_by('-title')
    
# class getalldevelopers(request):
#     products = .objects.all().values()

#     def get_queryset(self):   # for queries
#         return Project.objects.order_by('-title')