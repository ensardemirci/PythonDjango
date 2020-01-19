from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from .forms import PostForm


def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def post_update(request):
    return HttpResponse('Burası Post Update Sayfası')


def post_delete(request):
    return HttpResponse('Burası Post Delete Sayfası')
