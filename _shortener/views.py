from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.utils import timezone
from .models import Link
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'shortener/index.html')


def redirect_link(request, slug):
    link = get_object_or_404(Link, slug=slug)
    
    if link.expires_at and link.expires_at < timezone.now():
        raise Http404("This link has expired")
    
    link.access_count += 1
    link.save()
    return redirect(link.original_url)
