from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from account_app.models import User
from .models import Community

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def transition(request):
    user = request.user
    user.status = 1
    user.save()
    return render(request, 'musicpage_1.html')

@login_required(login_url='login')
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

@login_required(login_url='login')
def detail(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    return render(request, 'detail.html', {'community' : community})

@login_required(login_url='login')
def community(request):
    community_index = Community.objects.all().order_by('-created_at')
    return render(request, 'community.html', {'community_index': community_index})

@login_required(login_url='login')
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


@login_required(login_url='login')
def search(request):
    query = request.GET['query']
    if query:
        musician = User.objects.filter(name__contains=query) 
        return render(request, 'search.html', {'musician': musician})
    else:
        return render(request,'search.html')

@login_required(login_url='login')
def musician_list(request):
    musician_list = User.objects.filter(status__contains=1)
    return render(request, 'musician_list.html', {'musician_list': musician_list})

@login_required(login_url='login')
def comment(request, community_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.writer = request.user
        finished_form.post = get_object_or_404(Community, pk=community_id)
        finished_form.save()
    return redirect('detail', community_id)

@login_required(login_url='login')
def calendar(request):
    return render(request, 'calendar.html')
