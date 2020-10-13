import math

from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

from .forms import PostForm
from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from .models import Post


# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


# def contact(request):
#    return render(request, 'contact.html')


def post(request):
    posts = Post.objects.all().order_by('-post_modifydate')
    paginator = Paginator(posts, 3)
    page = int(request.GET.get('page', 1))
    pages = paginator.get_page(page)
    page_range = 5  # 페이지 범위 지정 예 1, 2, 3, 4, 5 / 6, 7, 8, 9, 10
    current_block = math.ceil(int(page) / page_range)  # 해당 페이지가 몇번째 블럭인가
    start_block = (current_block - 1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]
    return render(request, 'post.html', {'posts': pages, 'p_range': p_range})


def create(request):
    render(request, 'post_create.html')


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('post')
    else:
        form = PostForm()
    return render(request, 'post_edit.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            #            print(form.cleaned_data)
            #            post.cat_id = form.cleaned_data['cat_id']
            #            post.board_id = form.cleaned_data['board_id']
            #            post.post_notice = form.cleaned_data['post_notice']
            #            post.post_name = form.cleaned_data['post_name']
            #            post.post_content = form.cleaned_date['post_content']
            post = form.save()(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        post.delete()
        return render(request, 'post_delete.html')

    elif request.method == 'GET':
        return HttpResponse('잘못된 접근 입니다.')


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ksp6061@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success(request):
    return render(request, 'success.html')
