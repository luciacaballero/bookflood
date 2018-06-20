from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from django.views.generic.edit import CreateView
from bookflood.models import UserProfile, Book 

class BookView(View):
	model=Book

class BookList(BookView, ListView):
	template_name='book.html'

class BookDetail(BookView, DetailView):
	pass

class BookCreate(BookView, CreateView):
	fields=['title', 'author', 'genre', 'isbn', 'language']

def home(request):
	userprofiles=UserProfile.objects.all()
	data={'people':userprofiles}
	return render(request, 'home.html', data)

def view_person(request):
	person=UserProfile.objects.all()
	data={'person':person}
	return render(request, 'person.html', data)
