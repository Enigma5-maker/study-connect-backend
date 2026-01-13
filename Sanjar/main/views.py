from django.shortcuts import render, get_object_or_404
from .models import Article

def index (request):
    all_articles = Article.objects.all().order_by('-id')
    return render (request, 'main/index.html', {'articles':all_articles})

def post_detail(request, pk):
    post=get_object_or_404(Article, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})

# Create your views here.
