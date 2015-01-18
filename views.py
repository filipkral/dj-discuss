from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .models import Subject, Comment
from django.views.generic.list import ListView

from django.http import Http404


def home(request):
    return render(request, 'discuss/index.html')


def login_page(request):
    return render(request, 'discuss/login.html')


def login_user(request):
    myname = request.POST.get("myname")
    myword = request.POST.get("myword")
    # TODO: verify humanity by adding a checbox and ticking it on '#myname'.mouseenter
    user = authenticate(username=myname, password=myword)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('discuss:subject')
        else:
            # TODO: Add "The password is valid, but the account has been disabled!"
            return redirect('discuss:login')
    else:
        # TODO: Add invalid user details message.
        return redirect('discus:login')


class SubjectListView(ListView):
    model = Subject

    def get_context_data(self, **kwargs):
        context = super(SubjectListView, self).get_context_data(**kwargs)
        return context


def subject_detail(request, pk):
    try:
        sbj = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return render(request, 'discuss/404.html')
        #raise Http404
    
    return render(request, 'discuss/subject.html',  {'subject': sbj})
    
def add_comment(request):
    if not request.user.is_authenticated():
        return redirect('/discuss/login.html')
    
    if request.method == "POST":
        
        subjectid = request.POST.get("subjectid")
        title = request.POST.get("commenttitle")
        text = request.POST.get("commenttext")
        author = get_object_or_404(User, username=request.user.username)
        # TODO: verify input!
        
        s = Subject.objects.get(pk=int(subjectid))
        c = Comment(title=title, description=text, subject=s, owner=author)
        c.save()
    
    #return render(request, 'discuss/subject.html',  {'subject': s})
    return redirect('discuss:subject', pk=s.pk)
        
        

    
