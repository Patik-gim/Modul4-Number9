from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement99
from .forms import Advertisement99Form
# Create your views here.

def index(request):
    advertisements99 = Advertisement99.objects.all()
    context = {'advertisements99': advertisements99}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement99_post(request):
    if request.method == 'POST':
        form = Advertisement99Form(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement99(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = Advertisement99Form()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)