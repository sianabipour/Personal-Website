from django.shortcuts import render, redirect
from random import  choice
from Pages.models import Skill , Experience , Comment , Education, About , Portfoilio, CV

def homepage(request):
    skills= Skill.objects.all()
    experience = Experience.objects.all()
    about = About.objects.all()
    comments = Comment.objects.filter(published=True).order_by('-pk')[0:4]
    education = Education.objects.all()
    portfolio = Portfoilio.objects.all()
    cv = CV.objects.all()
    context = {
        "barname": skills ,
        "tajrobe": experience,
        "comments": comments,
        "tahsilat": education,
        "darbare":about,
        "portfolio":portfolio,
        "cv":cv,
    }
    return render(request,'index.html',context)

def contacts(request):
    if request.method == 'POST':
        Comment.objects.create(name=request.POST['name'],email=request.POST['email'],text=request.POST['text'])
        return redirect('Home')
    elif request.method == 'GET':
        return render(request, 'contacts.html')
    
