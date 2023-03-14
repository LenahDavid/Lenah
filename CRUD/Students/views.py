from django.shortcuts import render,redirect
from Students.forms import StudentsForm
from Students.models import Students

def std(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = StudentsForm()
    return render(request, 'index.html',{'form':form})

def view(request):
    students= Students.objects.all()
    return render(request,'view.html',{'students':students})

def delete(request, id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect('/view')

def edit(request, id):
    students = Students.objects.get(id=id)
   
    return render(request,'edit.html',{'students':students})
