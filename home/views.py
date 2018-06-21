from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):

    tasks = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'tasks':tasks,'form':form}

    return render(request, 'home/index.html', context)

@require_POST
def submit(request):

    form = TodoForm(request.POST)

    print(request.POST['text'])
    
    if form.is_valid():
        new_task = Todo(text=request.POST['text'])
        new_task.save()

    return redirect('index') 



def completeTodo(request, todo_id):
    
    todo = Todo.objects.get(pk=todo_id)
    
    todo.complete = True
    
    todo.save()

    return redirect('index')


def deleteDONE(request):
    
    Todo.objects.filter(complete__exact=True).delete()
    
    return redirect('index')

def deleteAll(request):

    Todo.objects.all().delete()

    return redirect('index')    