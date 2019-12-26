from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from django import forms

from .models import Blog
from comments.models import Comments

from comments.forms import CommentForm
from comments.models import Comments

# Create your views here.
def blog_view(request):
    obj = Blog.objects.all().order_by('id').reverse()
    
    content = {
        'blogs' : obj,
    }

    return render(request, "blog/index.html", content)

def blog_detail_view(request, id):
    #obj = Blog.objects.get(id=id)
    obj = get_object_or_404(Blog, id=id)
    comments = Comments.objects.filter(blog=obj).order_by('dateTime').reverse()
    all_obj = Blog.objects.exclude(id=obj.id).order_by('id').reverse()[:3]
    new_comment = {}
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #print(comment_form.cleaned_data)
            data = comment_form.cleaned_data
            data['blog'] = obj
            #print(data)
            Comments.objects.create(**data)
            new_comment = data
    else:
        comment_form = CommentForm()


    content = {
        'blog' : obj,
        'comments' : comments,
        'all_blogs' : all_obj,
        'form' : comment_form,
        'new_comment' : new_comment
    }
    return render(request, "blog/story.html", content)

def author_view(request, author):
    blogs = Blog.objects.filter(author=author).order_by('id').reverse()
    #print(blogs)
    content = {
        'author' : author,
        'blogs' : blogs,
    }
    return render(request, 'author/author.html', content)