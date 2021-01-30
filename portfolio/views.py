from django.shortcuts import render

from .models import Profile, Education, Project, Experince, Inbox, Skill
from .forms import InboxForm

def portfolio(request):
    profile = Profile.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.order_by('type')
    experiences = Experince.objects.order_by('pub_date')
    projects = Project.objects.order_by('pub_date')

    if request.method == "POST":
        form = InboxForm(request.POST)
        if form.is_valid():
            inbox_item = form.save()
            inbox_item.save()
    else:
        form = InboxForm()
    
    context = {
        'profile': profile[0],
        'educations': education,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
        'form': form
    }
        
    return render(request, 'portfolio.html', context)