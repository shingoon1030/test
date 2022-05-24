from django.shortcuts import render, redirect, get_object_or_404
from .models import freeB, comment
from django.utils import timezone
from .forms import freeBForm,commentForm
from django.contrib import auth
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request) :
    all_boards = freeB.objects.all().order_by("-date")
    paginator = Paginator(all_boards, 5)
    page = int(request.GET.get('page', 1))
    posts = paginator.get_page(page)
    return render(request, 'freeboard.html', {'posts':posts})

def new(request) :
    if request.method == 'POST' :
        form = freeBForm(request.POST)
        if form.is_valid() :
            post = freeB()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.nameINIT = User.get_username(request.user)
            post.name = "익명1"
            post.put_writer_name
            post.save()

            return  redirect('freeboard')
    else :
        form = freeBForm()
    return render(request, 'new.html', {'form' : form})

def new_comment(request, post_id) :
    filled_form = commentForm(request.POST)
    post_ = freeB(request.POST)

    if filled_form.is_valid() :
        
        finished_form = filled_form.save(commit = False)
        post_ = get_object_or_404(freeB, pk=post_id)
        finished_form.post = get_object_or_404(freeB, pk=post_id)
        username_current = User.get_username(request.user)
        finished_form.nameINIT = username_current
        if find_name(request, post_id, username_current) == -1:
            plus_name(request, post_id, username_current)
            finished_form.name = "익명"+str(find_name(request, post_id, username_current))
        else :
            finished_form.name = "익명"+str(find_name(request, post_id, username_current))
        finished_form.save()
        
    return redirect('detail', post_id)

def plus_name(request, post_id, newname) :
    post_ = freeB(request.POST)
    post_ = get_object_or_404(questionB, pk=post_id)
    if newname not in post_.nameTOname : 
        baseTable = post_.nameTOname
        post_.nameTOname = baseTable + newname + "|" + str(post_.nameCount+1)+ "/"
        post_.nameCount = post_.nameCount + 1
        post_.save()
        print(post_.nameTOname)
    else :
        print(newname + "은 존재합니다.")
    return None

def find_name(request, post_id, nametofind) :
    post_ = freeB(request.POST)
    post_ = get_object_or_404(questionB, pk=post_id)

    nameidx =  str(post_.nameTOname).find(nametofind)
    if nameidx == -1 :
        return -1
    nameidx = nameidx+len(nametofind)+1
    nameidxdelta = post_.nameTOname.find('/',nameidx)-1
    if nameidxdelta == nameidx :
        nameCount = int(post_.nameTOname[nameidx])
    else :
        nameCount = int(post_.nameTOname[nameidx:nameidxdelta+1])
    return nameCount

def detail(request, post_id) :
    blog_detail = get_object_or_404(freeB, pk=post_id)
    comment_form = commentForm()
    return render(request, 'detail.html', {'blog_detail':blog_detail , 'comment_form':comment_form})

def search(request):
    keyword = request.GET.get('q', " ")
    type = request.GET.get('type', " ")
    all_boards = freeB.objects.all().order_by("-date")
    
    if keyword :
        if len(keyword) > 1 :
            if type == 'all':
                searched_board =  all_boards.filter(Q (title__icontains=keyword) | Q (body__icontains=keyword) | Q (name__icontains=keyword))
            elif type == 'title_body':
                searched_board =  all_boards.filter(Q (title__icontains=keyword) | Q (body__icontains=keyword))
            elif type == 'title':
                searched_board =  all_boards.filter(title__icontains=keyword)    
            elif type == 'body':
                searched_board =  all_boardst.filter(body__icontains=keyword)    
            paginator = Paginator(searched_board, 5)
            page = int(request.GET.get('page', 1))
            posts = paginator.get_page(page)
            return render(request, 'freeboard.html', {'posts' : posts, 'keyword' : keyword, 'type' : type})
        else:
            messages.error(request, '검색어는 2글자 이상 입력해주세요.')

    paginator = Paginator(all_boards, 5)
    page = int(request.GET.get('page', 1))
    posts = paginator.get_page(page)
    return render(request, 'freeboard.html', {'posts' : posts})
    

def del_detail(request, post_id) :
    blog_detail = get_object_or_404(freeB, pk=post_id)
    if blog_detail.name == User.get_username(request.user) :
        blog_detail.delete()
        return redirect('/freeboard/')
    else :
        return detail(request, post_id)

def del_comment(request, post_id, comment_id):
    comment_todel = get_object_or_404(comment, pk=comment_id)
    if comment_todel.name == User.get_username(request.user) :
        comment_todel.delete()
        return redirect('detail', post_id)
    else :
        return redirect('detail', post_id)

def mustAuth(request) :
    return render(request, 'mustAuth.html')