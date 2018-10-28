from django.shortcuts import render

# Create your views here.
from posts.models import Post


def post_list(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, 'posts/post_list.html', context)
