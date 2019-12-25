from django.shortcuts import render, get_object_or_404

from .models import Blog
from comments.forms import CommentForm
# Create your views here.
def blog_view(request):
    obj = Blog.objects.all().order_by('date').reverse()
    
    content = {
        'blogs' : obj,
    }

    return render(request, "blog/index.html", content)

def blog_detail_view(request, id):
    #obj = Blog.objects.get(id=id)
    obj = get_object_or_404(Blog, id=id)
    all_obj = Blog.objects.all().order_by('date').reverse()[:3]

    comment_form = CommentForm()

    if request.method == "POST":
        print(request.POST.get('comment'))
    content = {
        'blog' : obj,
        'all_blogs' : all_obj,
        'form' : comment_form,
    }
    return render(request, "blog/story.html", content)