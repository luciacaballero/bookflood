from django.shortcuts import render
from bookflood.models import UserProfile

def home(request):
	userprofiles=UserProfile.objects.all()
	data={'people':userprofiles}
	return render(request, 'home.html', data)