from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Subject, Comment

from django.http import Http404

def home(request):
    return render(request, 'discuss/index.html')
    
def subject_list(request):
    # TODO: get subject list data
    return render_to_response('discuss/subjects.html', {"subjects": []})
    
def subject_detail(request, pk):
    try:
        sbj = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return render(request, 'discuss/404.html')
        #raise Http404
    return render(request, 'discuss/subject.html',  {'subject': sbj})
    

