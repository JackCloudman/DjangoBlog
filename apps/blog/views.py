from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
def home(request,page=0):
    page = int(page)
    if page==0:
        posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).order_by('-fecha_publicado')[:4]
    else:
        posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).order_by('-fecha_publicado')[page*4:page*4+4]
    
    total = len(Post.objects.filter(fecha_publicado__lte=timezone.now()))
    post_antiguos = (page*4+4) <=total
    post_recientes = page>=1
    anterior = page-1
    siguiente = page+1
    return render(request, 'index.html', {'posts':posts,'post_antiguos':post_antiguos,'post_recientes':post_recientes,
                        'anterior':anterior,'siguiente':siguiente})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
def error_404(request):
    return page_not_found(request, '404.html')


