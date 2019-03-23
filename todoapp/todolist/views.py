from django.shortcuts import render, redirect
from todolist.models import *
from django.http import HttpResponse

def index(request):
	todos = TodoList.objects.all()
	categories = Category.objects.all()

	if request.method == 'POST':
		if "taskAdd" in request.POST:
			title = request.POST["description"]
			date = str(request.POST["date"])
			category = request.POST["category_select"]
			content = title + " -- " + date + " " + category

			Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
			Todo.save()
			return redirect('/')

		if "taskDelete" in request.POST:
			try:
				checkedlist = request.POST["checkedbox"]
				for todo_id in checkedlist:
					todo = TodoList.objects.get(id=int(todo_id))
					todo.delete()
			except:
				return HttpResponse('<center><h2 class="display-4" style="margin-top: 30%;">You have not selcted any task to delete</h2><br><br><a href="">Return to Home</a></center>')
	return render(request, "index.html", {"todos": todos, "categories": categories})