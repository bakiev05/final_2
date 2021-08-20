from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory

from apps.posts.models import Post, PostImage

from apps.posts.forms import PostForm, PostImageForm
from apps.comments.models import Reply


def data(request):
    return render(request, 'index.html', locals())


def blog_post(request):
    posts = Post.objects.all()
    return render(request, 'posts/blog.html', locals())




def create_post(request):
    form = PostForm(request.POST, None)
    PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImageForm, extra=1)
    if form.is_valid():
        post = form.save()
        formset = PostImageFormSet(request.POST, request.FILES, instance=post)
        if formset.is_valid():
            formset.save()
            return redirect('blog_post')
    formset = PostImageFormSet()
    return render(request, 'posts/create_post.html', locals())


def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST, None, instance=post)
    PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImageForm, extra=1)
    if form.is_valid():
        post = form.save()
        formset = PostImageFormSet(request.POST, request.FILES, instance=post)
        if formset.is_valid():
            formset.save()
            return redirect('blog_post')
    formset = PostImageFormSet(instance=post)
    return render(request, 'posts/update.html', locals())


def delete_post(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('blog_post')
    return render(request, 'posts/delete.html', locals())


def post_detail(request, id):
    post = Post.objects.get(id=id)
    if 'reply' in request.POST:
        id = request.POST.get('post_id')
        post = Post.objects.get(id=id)
        text = request.POST.get('reply_text')
        reply = Reply.objects.create(text=text, post=post, user=request.user)
        return redirect('post_detail')
    return render(request, 'posts/detail.html', {"post": post})
