from django.shortcuts import render, redirect, get_object_or_404
from .models import lectureB
from django.utils import timezone
from .forms import lectureBForm
from django.contrib import auth
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request) :
    all_boards = lectureB.objects.all().order_by("-date")
    paginator = Paginator(all_boards, 5)
    page = int(request.GET.get('page', 1))
    posts = paginator.get_page(page)
    return render(request, 'lectureboard.html', {'posts':posts})

def new(request) :
    if request.method == 'POST' :
        form = lectureBForm(request.POST)
        if form.is_valid() :
            post = lectureB()
            post.title = form.cleaned_data['title']
            post.titleL = form.cleaned_data['titleL']
            post.titleT = form.cleaned_data['titleT']
            post.body = form.cleaned_data['body']
            post.name = User.get_username(request.user)
            post.save()
            return  redirect('lectureboard')
    else :
        form = lectureBForm()
    return render(request, 'newL.html', {'form' : form})

def detail(request, post_id) :
    blog_detail = get_object_or_404(lectureB, pk=post_id)
    return render(request, 'detailL.html', {'blog_detail':blog_detail})

def search(request):
    keyword = request.GET.get('q', " ")
    type = request.GET.get('type', " ")
    all_boards = lectureB.objects.all().order_by("-date")
    
    if keyword :
        if len(keyword) > 1 :
            if type == 'all':
                searched_board =  all_boards.filter(Q (title__icontains=keyword) | Q (body__icontains=keyword) | Q (name__icontains=keyword))
            elif type == 'titleL':
                searched_board =  all_boards.filter(Q (titleL__icontains=keyword))
            elif type == 'titleT':
                searched_board =  all_boards.filter(Q (titleT__icontains=keyword))
            elif type == 'title':
                searched_board =  all_boards.filter(title__icontains=keyword)    
            elif type == 'body':
                searched_board =  all_boardst.filter(body__icontains=keyword)    
            paginator = Paginator(searched_board, 5)
            page = int(request.GET.get('page', 1))
            posts = paginator.get_page(page)
            return render(request, 'lectureboard.html', {'posts' : posts, 'keyword' : keyword, 'type' : type})
        else:
            messages.error(request, '검색어는 2글자 이상 입력해주세요.')

    paginator = Paginator(all_boards, 5)
    page = int(request.GET.get('page', 1))
    posts = paginator.get_page(page)
    return render(request, 'lectureboard.html', {'posts' : posts})
    

def del_detail(request, post_id) :
    blog_detail = get_object_or_404(lectureB, pk=post_id)
    if blog_detail.name == User.get_username(request.user) :
        blog_detail.delete()
        return redirect('/lectureboard/')
    else :
        return detail(request, post_id)
