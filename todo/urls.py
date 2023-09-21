
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('add_items/',views.add_todo_items,name='add_todo_items'),
    path('edit_item/<int:pk>',views.edit_todo_item,name='edit_todo_item'),
    path('del_todo/<int:pk>',views.del_todo_item,name='del_todo_item'),
]