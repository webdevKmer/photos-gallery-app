from django.shortcuts import render, redirect

from .forms import AddPhotoForm, NewCategoryForm
from .models import Category, Photo

# Create your views here.

def gallery(request):
  categories = Category.objects.all()
  category = request.GET.get('category')
  print(category)
  photos = Photo.objects.all()
  if category == None:
    photos = Photo.objects.all()
  else:
    photos = Photo.objects.filter(category__name=category)
  context = { 'photos' : photos, 'categories' : categories }
  return render(request, 'photos/index.html', context)

def view_photo(request, pk):
  photo = Photo.objects.get(id=pk)
  context = { 'photo' : photo }
  return render(request, 'photos/view_photo.html', context)

def add_photo(request):
  if request.method == 'POST':
    form = AddPhotoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('photos:gallery')
  else :
    form = AddPhotoForm()
  context = { 'form' : form }
  return render(request, 'photos/add_photo.html', context)

def new_category(request):
  if request.method == 'POST':
    form = NewCategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('photos:add')
  else :
    form = NewCategoryForm()
  context = { 'form' : form }
  return render(request, 'photos/add_category.html', context)