from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def todolist(request):
     if request.method=="POST":
          form = TaskForm(request.POST or None)
          if form.is_valid():
               form.save()
          messages.success(request,("New Task Added!"))
          return redirect('todolist')
     else:
          all_tasks = TaskList.objects.all()
          paginator = Paginator(all_tasks, 5)
          page = request.GET.get('pg')
          all_tasks=paginator.get_page(page)
          return render(request,'todolist.html',{'all_tasks': all_tasks})

def task_delete(request, task_id):
     task = TaskList.objects.get(pk=task_id)
     task.delete()
     return redirect('todolist')

def task_edit(request, task_id):
     if request.method=="POST":
          task = TaskList.objects.get(pk=task_id)
          form = TaskForm(request.POST or None, instance= task)
          if form.is_valid():
               form.save()
          messages.success(request,("Task Updated"))
          return redirect('todolist')
     else:
          task_obj = TaskList.objects.get(pk=task_id)
          return render(request,'edit.html', {'task_obj': task_obj})

def task_complete(request, task_id):
     task = TaskList.objects.get(pk=task_id)
     task.done = True
     task.save()
     return redirect('todolist')

def task_pending(request, task_id):
     task = TaskList.objects.get(pk=task_id)
     task.done = False
     task.save()
     return redirect('todolist')



     

def contact(request):
     context = {
          'contact_text':"Welcome to contact page",
     }
     return render(request,'contact.html',context)

def about(request):
     context = {
          'about_text':"Welcome to about us page",
     }
     return render(request,'about.html',context)

def index(request):
     context = {
          'index_text':"Welcome to Index page",
     }
     return render(request,'index.html',context)

