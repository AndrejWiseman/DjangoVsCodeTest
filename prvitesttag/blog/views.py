from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from .models import Post
from .forms import PostForm
from taggit.models import Tag

# Create your views here.
def home(request):
    posts = Post.objects.all()

    common_tags = Post.tags.most_common()
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()


    context = {
        'posts':posts,
        'common_tags': common_tags,
        'form': form
    }
    return render(request, 'blog/home.html', context)


def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)



def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
    }
    return render(request, 'blog/home.html', context)