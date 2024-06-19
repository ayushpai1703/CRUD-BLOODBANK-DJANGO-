from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Person
from .forms import LogForm

def welcome(request): 
    return render(request, 'welcome.html' )


def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})

def person_create(request):
    form = LogForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = LogForm()
    context = {'form': form}
    return render(request, 'person_form.html', context)

def person_update(request, pk):
    person = Person.objects.get(pk=pk)
    form = LogForm(request.POST or None, instance=person)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = LogForm(instance=person)
    context = {'form': form}
    return render(request, 'person_form.html', context)

def delete_person(request, pk):
    context = {} 
    try:
        person = Person.objects.get(pk=pk)
        context['person'] = person
    except ObjectDoesNotExist:
        messages.error(request, 'Person not found.')
        return render(request, 'person_list.html')

    if request.method == 'POST':
        person.delete() 
        messages.success(request, 'Successfully deleted')
        return render(request, 'person_list.html')

    return render(request, 'delete_person.html', context)
   
def person_show(request):
    query = request.GET.get('q')
    if query:
        donors = Person.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(city__icontains=query) |
            Q(blood_type__icontains=query)
        )
    else:
        donors = Person.objects.all()
    return render(request, 'person_show.html', {'donors': donors, 'query': query})
  