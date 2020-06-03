from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .form import BlogForm
# Create your views here.


def create(request, blog_id):
    update_blog = get_object_or_404(Blog, pk=blog_id)
    update_blog.title = request.POST['title']
    update_blog.pub_date = timezone.datetime.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('detail', update_blog.id)


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})


def new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('home')
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form': form})


def update(request, blog_id):
    update_blog = get_object_or_404(Blog, pk=blog_id)
    update_blog.title = request.POST['title']
    update_blog.pub_date = timezone.datetime.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return render('detail', update_blog.id)


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.pub_date = timezone.datetime.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('/main/'+str(new_blog.id))


def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog': edit_blog})


def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')


def seeun(request):
    return render(request, 'seeun.html')

def seyeon(request):
    return render(request, 'seyeon.html')
