#from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from blog.models import Blog

from comments.models import Comments

# Create your views here.
def home_view(request, *args, **kwargs):
    featured = Blog.objects.all().order_by('id').reverse()[:1]
    all_blogs = Blog.objects.all().order_by('-id')
    recent_five_blogs = Blog.objects.exclude(id=None).order_by('id').reverse()[:5]
    all_comments = Comments.objects.all()
    #print(recent_five_blogs)
    result = {}

    for comment in all_comments: 
        if comment.parent == None:
            if comment.blog in result:
                result[comment.blog] += 1
            else:
                result[comment.blog] = 1
        else:
            if comment.parent.blog in result:
                result[comment.parent.blog] += 1
            else:
                result[comment.parent.blog] = 1
    result = sorted(result.items(), key=lambda kv: kv[1], reverse=True)

    result = result[:4]

    result = dict(result)

    for blog in all_blogs:
        if len(result) == 4:
            break;
        if blog in result:
            continue;
        else:
            result[blog] = 0


    result = dict(result)
    #print(result)
    content = {
        'featured' : featured,
        'trending' : result,
        'all_blogs' : all_blogs,
        'recent_five_blogs' : recent_five_blogs,
    }

    return render(request, 'home/landingpage.html', content)

def about_view(request):
    return render(request, 'pages/about.html', {})

def brave_view(request):
    return redirect("https://tech-snippets.azurewebsites.net/static/.well-known/brave-rewards-verification.txt")
