from django.contrib import messages
from django.core.mail import message
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

from .form import Sutdent_info_from, Semester1_marks_form
from .models import Sutdent_info, Semester1_marks
from django.forms import formset_factory


# def add(request):
#     student_formset = formset_factory(Sutdent_info_from, extra=3)
#     if request.method == 'POST':
#         form = student_formset(request.POST, request.FILES)
#         if form.is_valid():
#             for f in form:
#                 f.save()
#             return redirect('/')
#     else:
#         form = student_formset()
#     student_info = Sutdent_info.objects.all()
#     return render(request, 'sms/main.html', {'form': form, 'student_info': student_info})

def add(request):
    if request.method == 'POST':
        form = Sutdent_info_from(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Sutdent_info_from()
    student_info = Sutdent_info.objects.all()
    return render(request, 'sms/main.html', {'form': form, 'student_info': student_info})


def display(request):
    student_info = Sutdent_info.objects.all()
    return render(request, 'sms/main.html', {'student_info': student_info})


def details(request, student_id):
    detail = get_object_or_404(Sutdent_info, pk=student_id)
    if request.method == 'POST':
        form = Semester1_marks_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Semester1_marks_form()
    context = {'detail': detail, 'form': form}
    return render(request, 'sms/details.html', context)


def delete(request, student_id):
    student_delete = get_object_or_404(Sutdent_info, pk=student_id)
    if request.method == 'POST':
        student_delete.delete()
        return redirect('/')
    context = {'student_delete': student_delete}
    return render(request, 'sms/delete.html', context)


def update(request, student_id):
    get_info = Sutdent_info.objects.get(pk=student_id)
    form = Sutdent_info_from(instance=get_info)
    if request.method == "POST":
        form = Sutdent_info_from(request.POST, request.FILES, instance=get_info)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'get_info': get_info}
    return render(request, 'sms/update.html', context)


def add_marks(request, student_id):
    get_info = get_object_or_404(Sutdent_info, pk=student_id)
    if request.method == 'POST':
        form = Semester1_marks_form(request.POST)
        if form.is_valid():
            student_marks = form.save(commit=False)
            student_marks.student = get_info
            student_marks.save()
            return redirect(reverse('add_marks', kwargs={'student_id': student_id}))
    else:
        form = Semester1_marks_form()
    context = {'get_info': get_info, 'form': form}
    return render(request, 'sms/add_marks.html', context)
