from django.urls import path 
from . import views 


urlpatterns = [
    path("todos", views.todo_list),
    path("todos/<int:pk>", views.todo_detail),
    path('todos/delete-all/', views.delete_all_todos, name='delete_all_todos'),
]