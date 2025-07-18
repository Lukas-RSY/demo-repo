from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

from django.contrib.auth import logout

def index(request):
    items = Item.objects.all()[0:3]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories' : categories, 
        'items' : items,
    })

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('/login/')
	else:	
		form = SignupForm()

	return render(request, 'core/signup.html', {
		'form': form
	})

def logout_view(request):
    logout(request)
    return redirect('core:index')

def contact(request):
    return render(request, 'core/contact.html')