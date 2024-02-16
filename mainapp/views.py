from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mainapp.models import Student


class StudentListView(ListView):
    model = Student


# def index(request):
#     student_list = Student.objects.all()
#     context = {
#         'object_list': student_list,
#         'title':'Главная'
#     }
#
#     return render(request, 'mainapp/index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name},{email},{message}")
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)


class StudentDetailView(DetailView):
    model = Student


# def view_student(request, pk):
#     student_item = get_object_or_404(Student, pk=pk)
#     context = {
#         'object': student_item
#     }
#     return render(request, 'mainapp/student_detail.html', context)


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('mainapp:index')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('mainapp:index')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('mainapp:index')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True
    student_item.save()

    return redirect(reverse('mainapp:index'))
