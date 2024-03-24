from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


def student_view(request):
    template_name = 'curd_app/stu_info.html'
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = Student.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def update_view(request):
    obj = Student.objects.get()
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "curd_app/stu_info.html"
    context = {"form": form}
    return render(request, template_name, context)


def delete_view(request):
    obj = Student.objects.get()
    if request.methof == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, "curd_app/confirm.html")
