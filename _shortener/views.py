from django.shortcuts import render, redirect, get_object_or_404
from .models import Link
from .forms import LinkForm


def create_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save()
            return render(request, 'shortener/success.html', {'link': link})
    else:
        form = LinkForm()
    return render(request, 'shortener/create.html', {'form': form})

def redirect_link(request, slug):
    link = get_object_or_404(Link, slug=slug)
    return redirect(link.original_url)
