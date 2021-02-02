from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from .models import Post
# Create your views here.
def index(req):
    posts = Post.objects.order_by('created_date')[:4]
    context = {'posts': posts}
    return JsonResponse(context, JSONEncoder)

def post(req, post_id):
    try:
        post = Post.objects.get(id=post_id)
        context = {
            'post': post
        }
        return render(req, 'Post/post.html', context)
    except Post.DoesNotExist:
        return render(request=req, status=400)
