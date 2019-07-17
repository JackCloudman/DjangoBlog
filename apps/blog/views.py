from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.utils import timezone
from django.db.models import Q
def post_list(request,page=0):
    page = int(page)
    posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).exclude(slug__exact=None).order_by('-fecha_publicado')
    total = posts.count()
    if page==0:
        posts = posts[:4]
    else:
        posts = posts[page*4:page*4+4]

    post_antiguos = (page*4+4) <total
    post_recientes = page>=1
    anterior = page-1
    siguiente = page+1
    return render(request, 'index.html', {'posts':posts,'post_antiguos':post_antiguos,'post_recientes':post_recientes,
                        'anterior':anterior,'siguiente':siguiente})
def search_list(request):
    page = request.GET.get("page")
    query = request.GET.get("q")
    if not query:
        return redirect("/")
    posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).exclude(slug__exact=None)
    posts = posts.filter(
                        Q(titulo__icontains=query) |
                        Q(descripcion__icontains=query) |
                        Q(tags__icontains=query) |
                        Q(contenido__icontains=query) |
                        Q(autor__first_name__icontains=query) |
                        Q(autor__last_name__icontains=query)).distinct().order_by('-fecha_publicado')
    total = posts.count()
    if page:
        page = int(page)-1
        posts = posts[page*4:page*4+4]
    else:
        page=0
        posts = posts[:4]
    post_antiguos = (page*4+4) <total
    post_recientes = page>=1
    anterior = page-1
    siguiente = page+1
    contexto = {'posts':posts,
                'post_antiguos':post_antiguos,
                'post_recientes':post_recientes,
                'anterior':anterior+1,
                'siguiente':siguiente+1}
    return render(request, 'search.html',contexto)
def post_detail(request, pk,title=None):
    post = Post.objects.filter(fecha_publicado__lte=timezone.now(),pk=pk).exclude(slug__exact=None)
    if not post:get_object_or_404(Post,pk=pk)
    post = post[0]
    if not title or title!=post.slug:
        return redirect("/post/%s/%s/"%(pk,post.slug))
    post.post_views=post.post_views+1
    post.save()
    return render(request, 'post_detail.html', {'post': post})
def error_404(request):
    return page_not_found(request, '404.html')
