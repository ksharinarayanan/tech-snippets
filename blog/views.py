from django.shortcuts import render, get_object_or_404
from django.db.models import Q


from django import forms
# model : blog
from .models import Blog

# model : comments
from comments.models import Comments
from comments.forms import CommentForm
from comments.models import Comments

# Create your views here.



def blog_view(request):
    obj = Blog.objects.all().order_by('id').reverse()
    
    content = {
        'blogs' : obj,
    }

    return render(request, "blog/blogs.html", content)

def blog_detail_view(request, id):
    #obj = Blog.objects.get(id=id)
    blog = get_object_or_404(Blog, id=id)
    comments = Comments.objects.filter(blog=blog).order_by('dateTime').reverse()
    all_blogs = Blog.objects.exclude(id=blog.id).order_by('id').reverse()[:3]

    result = {}

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            if 'parent_id' in request.POST:
                Comments.objects.create(
                    name = request.POST.get("name"),
                    comment = request.POST.get("comment"),
                    email = request.POST.get("email"),
                    parent = Comments.objects.get(id=request.POST.get("parent_id")),
                )
                #print(Comments.objects.get(name="CSK"))
            else:
                data = comment_form.cleaned_data
                data['blog'] = blog
                Comments.objects.create(**data)

    comment_form = CommentForm()

    for c in comments:
        reply = Comments.objects.filter(parent=c).order_by('dateTime')

        for r in reply:
            if c in result:
                result[c].append(r)
            else:
                result[c] = [r]

    content = {
        'blog' : blog,
        'comments' : comments,
        'all_blogs' : all_blogs,
        'form' : comment_form,
        'result' : result,
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