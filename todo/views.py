from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import ToDoItemForm
from . models import ToDoItems
from django.template import loader

# Create your views here.
def home(request):
    todoitems=ToDoItems.objects.all()
    template=loader.get_template('todo_list.html')
    context={
        'todoitems':todoitems,
    }
    return HttpResponse(template.render(context,request))
def add_todo_items(request):
    if request.method=='POST':
        form=ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ToDoItemForm()
        template=loader.get_template('add_todo_items.html')
        context={
            'form':form,
        }
    return HttpResponse(template.render(context,request))
def edit_todo_item(request,pk):
    todo_item=ToDoItems.objects.get(pk=pk)
    if request.method=='POST':
        form=ToDoItemForm(request.POST,instance=todo_item)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form=ToDoItemForm(instance=todo_item)
        template=loader.get_template('edit_todo_item.html')
        context={
            'form':form,
        }
        return HttpResponse(template.render(context,request))
def del_todo_item(request,pk):
    todo_item=ToDoItems.objects.get(pk=pk)
    if request.method=='POST':
        todo_item.delete()
        return redirect('home')
    else:
        template=loader.get_template('del_todo_item.html')
        context={
            'todo_item':todo_item,
        }
        return HttpResponse(template.render(context,request))