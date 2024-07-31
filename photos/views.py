from django.shortcuts import render

# Create your views here.

def gallery(request):
  return render(request, 'photos/index.html', {})

def view_photo(request, pk):
  return render(request, 'photos/view_photo.html', {'pk':pk})

def add_photo(request):
  return render(request, 'photos/add_photo.html', {})