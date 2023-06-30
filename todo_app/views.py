from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import ToDoItems, ToDoList


class ToDoListView(ListView):
    model = ToDoList
    template_name = 'todo_app/index.html'

class ItemListView(ListView):
    model = ToDoItems
    template_name = 'todo_app/todo_list.html'

    def post(self, request, *args, **kwargs):
        obj_id = request.POST.get('done_id', None)
        obj = ToDoItems.objects.get(id=obj_id)
        obj.done = True
        obj.save()
        return self.get(request, *args, **kwargs)

    def get_queryset(self):
        return ToDoItems.objects.filter(todo_list_id=self.kwargs['list_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs['list_id'])
        return context
    
class ListCreate(CreateView):
    model = ToDoList
    fields = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add a new list'
        return context
    
class ItemCreate(CreateView):
    model = ToDoItems
    fields = ['todo_list', 'title', 'description', 'due_date']

    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        initial_data['todo_list'] = todo_list
        return initial_data
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        context['title'] = 'Create a new item'
        return context
    
    def get_success_url(self) -> str:
        return reverse('list', args=[self.object.todo_list_id])
    
class ItemUpdate(UpdateView):
    model = ToDoItems
    fields = ['todo_list', 'title', 'description', 'due_date', 'done']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        context['title'] = 'Edit item'
        return context
    
    def get_success_url(self) -> str:
        return reverse('list', args=[self.object.todo_list_id])

class ListDelete(DeleteView):
    model = ToDoList
    success_url = reverse_lazy('index')

class ItemDelete(DeleteView):
    model = ToDoItems

    def get_success_url(self) -> str:
        return reverse_lazy('list', args=[self.kwargs['list_id']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context
    