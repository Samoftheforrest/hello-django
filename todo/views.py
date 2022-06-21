from django.shortcuts import render


# Create your views here.
def get_todo_list(request):
    """
    Renders the todo list page.
    """
    return render(request, "todo/todo_list.html")
