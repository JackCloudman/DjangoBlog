from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
def home(request):
    posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_publicado')    
    return render(request, 'index.html', {'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
# Create your views here.
