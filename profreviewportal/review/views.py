from django.shortcuts import render, redirect
from .models import Review, Prof, Course
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import get_list_or_404, get_object_or_404
from accounts.models import LikesCount
from dal import autocomplete
from django.contrib.auth.models import User
from .filters import ReviewFilter
from django.http import HttpResponseRedirect
# Create your views here.


class CodeAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Course.objects.all()

        if self.q:
            qs = qs.filter(courseName__istartswith=self.q)

        return qs


class ProfAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Prof.objects.all()

        if self.q:
            qs = qs.filter(profname__istartswith=self.q)

        return qs


@login_required(login_url="/accounts/login")
def add_review(request):
    if request.method == 'POST':
        form = forms.AddReview(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('review:search')
            # return HttpResponse('added')
    else:
        form = forms.AddReview()
    return render(request, 'review/add_review.html', {'form': form})


def review_list(request):
    reviews = Review.objects.all().order_by('-date')
    return render(request, 'review/course_list.html', {'reviews': reviews})


def search(request):
    review_filter = ReviewFilter(request.GET, queryset=Review.objects.all())
    ratings = LikesCount.objects.all()
    return render(request, 'review/search.html', {'filter': review_filter, 'ratings': ratings})


def add_prof(request):
    if request.method == 'POST':
        form = forms.AddProf(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profcheck = data['profname']
            profs = Prof.objects.all()
            for prof in profs:
                if prof.profname == profcheck:
                    return render(request, 'review/already_there.html')
            # save article to db
            form.save()
            return redirect('review:search')
    else:
        form = forms.AddProf()
    return render(request, 'review/add_prof.html', {'form': form})


def add_course(request):
    if request.method == 'POST':
        form = forms.AddCourse(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            coursecheck = data['courseName']
            courses = Course.objects.all()
            for course in courses:
                if course.courseName == coursecheck:
                    return render(request, 'review/already_there.html')
            # save article to db
            form.save()
            return redirect('review:search')
    else:
        form = forms.AddCourse()
    return render(request, 'review/add_course.html', {'form': form})


def add_report(request):
    post = Review.objects.get(id=request.POST['post_report'])
    if post.report == False:
        post.report = True
    post.save()
    return render(request, 'review/reported.html')


def like_post(request):
    post = Review.objects.get(id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        tempuser = post.author
        likeduser = LikesCount.objects.get(user=tempuser)
        likeduser.userlikes = likeduser.userlikes-1
        likeduser.save()
    else:
        post.likes.add(request.user)
        tempuser = post.author
        likeduser = LikesCount.objects.get(user=tempuser)
        likeduser.userlikes = likeduser.userlikes+1
        likeduser.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def dis_post(request):
#     post2 = Review.objects.get(id=request.POST.get('post_id2'))
#     if post2.dislikes.filter(id=request.user.id).exists():
#         post2.dislikes.remove(request.user)
#         tempuser = post2.author
#         dislikeduser = LikesCount.objects.get(user=tempuser)
#         dislikeduser.userlikes = dislikeduser.userlikes+1
#         dislikeduser.save()
#     else:
#         post2.dislikes.add(request.user)
#         tempuser = post2.author
#         dislikeduser = LikesCount.objects.get(user=tempuser)
#         dislikeduser.userlikes = dislikeduser.userlikes-1
#         dislikeduser.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# HTML FORM FOR DISLIKE:
    # <!-- <form action="{% url 'review:dis_post' %}" method="POST">
    #     {% csrf_token %}

    #     {% if request.user in obj.dislikes.all and not request.user in obj.likes.all %}
    #     <button type="submit" name="post_id2" value="{{ obj.id }}"> Remove Dislike </button>
    #     {% elif not request.user in obj.dislikes.all and not request.user in obj.like.all  %}
    #     <button type="submit" name="post_id2" value="{{ obj.id }}"> Dislike </button>
    #     {% else %}
    #     {% endif %}
    # </form> -->
