from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from account_app.models import User, Concert
from .models import Community
from datetime import date

# Create your views here.

def home(request):
    # dateField가 오늘 날짜인 공연만 전송 
    concerts = Concert.objects.filter(date__range=[date.today(), date.today()]).values().all()    
    return render(request, 'home.html', {'concerts': concerts})

@login_required(login_url='/accounts/naver/login/')
def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    else:
        community = Community()
        community.author = request.user
        community.content = request.POST["content"]
        community.photo = request.FILES.get('photo')
        community.save()
        return redirect('detail', community.id)

@login_required(login_url='/accounts/naver/login/')
def detail(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    return render(request, 'detail.html', {'community' : community})

@login_required(login_url='/accounts/naver/login/')
def community(request):
    community_index = Community.objects.all().order_by('-created_at')
    return render(request, 'community.html', {'community_index': community_index})

@login_required(login_url='/accounts/naver/login/')
def like(request, community_id):
    like_b = get_object_or_404(Community, id=community_id)
    if request.user in like_b.like.all():
        like_b.like.remove(request.user)
        like_b.like_count -= 1
        like_b.save()
    else:
        like_b.like.add(request.user)
        like_b.like_count += 1
        like_b.save()
    return redirect('detail', community_id)

@login_required(login_url='/accounts/naver/login/')
def search(request):
    query = request.GET['query']
    if query:
        musician_list = User.objects.filter(status__contains=1, name__contains=query).order_by("?")
        return render(request, 'search.html', {'musician_list': musician_list, 'query' : query})
    else:
        error = "검색어를 입력받지 못했습니다"
        return render(request,'search.html', {'error' : error})

@login_required(login_url='/accounts/naver/login/')
def musician_list(request):
    musician_list = User.objects.filter(status__contains=1).order_by("?")
    return render(request, 'musician_list.html', {'musician_list': musician_list})

@login_required(login_url='/accounts/naver/login/')
def comment(request, community_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.writer = request.user
        finished_form.post = get_object_or_404(Community, pk=community_id)
        finished_form.save()
    return redirect('detail', community_id)

@login_required(login_url='/accounts/naver/login/')
def calendar(request):
    return render(request, 'calendar.html')
