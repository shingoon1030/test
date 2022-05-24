from django.shortcuts import render, redirect, get_object_or_404
from freeboard.models import freeB, comment
from questionboard.models import questionB, comment
from django.utils import timezone
from freeboard.forms import freeBForm,commentForm
from django.contrib import auth
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
def home(request) :
    all_boards = freeB.objects.all().order_by("-date")
    paginator = Paginator(all_boards, 5)
    page = int(request.GET.get('page', 1))
    posts = paginator.get_page(page)
    
    all_boardsQ = questionB.objects.all().order_by("-date")
    paginatorQ = Paginator(all_boardsQ, 5)
    pageQ = int(request.GET.get('page', 1))
    postsQ = paginatorQ.get_page(page)
    
    return render(request, 'home.html', {'posts':posts , 'postsQ':postsQ})