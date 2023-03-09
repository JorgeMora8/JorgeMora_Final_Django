from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..forms.Forms import *
from django.contrib.auth.models import User
from ..models import *


@login_required
def homePage(request): 
    return render(request, "homepage.html")

@login_required
def competition(request): 
    competitions = Competition.objects.all()

    return render(request, "competition.html", {"competitions": competitions})

@login_required
def blog(request): 
    query = request.GET.get('q')
    
    if query != None: 
        blog_list = Blog.objects.filter(category__name = query)
    else: 
        blog_list = Blog.objects.all()
    
    blog_type = Blog_type.objects.all()
    
    context = {"blog_list": blog_list, 
               "blog_types": blog_type}
    return render(request, "blog.html" ,context)

@login_required
def blogDetail(request, pk):
    form = ReviewsBlogsForm(initial={"name": request.user}) 
    blog_detail = Blog.objects.filter(id = pk).first()
    review_from_blog = Review.objects.filter(Category = blog_detail)

    if request.method == "POST": 
        form = ReviewsBlogsForm(request.POST)
        if form.is_valid(): 
            form.save()

            context = {"blog": blog_detail, 
                       "reviews": review_from_blog, 
                       "form_review": form}
            
            return render(request, "blogDetail.html", context)
        
    context = {"blog": blog_detail, 
               "reviews": review_from_blog, 
               "form_review": form}
    
    return render(request, "blogDetail.html", context)

def create_competition(request): 
    form = CreateCompetition()
    if request.method == 'POST': 
        form = CreateCompetition(request.POST)
        if form.is_valid(): 
            form.save()
        else: 
            context = {"form": form, 
                       "message":"Invalidad data types, please check..."}
            
            return render(request, "createCompetition.html", context)
    else: 
        return render(request, "createCompetition.html", {"form": form})


@login_required
def competition_detail(request, pk): 
    form_competitionEnroll = CompetitionEnrollForm(initial={"user_linked": request.user})
    competition = Competition.objects.filter(id = pk).first()
    competitors = Competitors.objects.filter(competition_in=competition)
    
    if request.method == 'POST': 
        form_competitionEnroll = CompetitionEnrollForm(request.POST, request.FILES)
        if form_competitionEnroll.is_valid(): 
            form_competitionEnroll.save()
            
            context = {"competitors": competitors, 
                       "competition_detail": competition, 
                       "form": form_competitionEnroll}
            
            return render(request, "competitionDetail.html", context) 

    else:
         context = {"competitors": competitors, 
                    "competition_detail": competition, 
                    "form": form_competitionEnroll}
         
         return render(request, "competitionDetail.html", context) 
    
    context = {"competitors": competitors, 
               "competition_detail": competition}
    
    return render(request, "competitionDetail.html", context)

@login_required
def admin_page(request): 
    competition_list = Competition.objects.all()
    competitors_list = Competitors.objects.all()
    review_list = Review.objects.all()
    blog_list = Blog.objects.all() 

    context =  {
                "blog_list": blog_list,
                "review_list": review_list, 
                "competition_list": competition_list, 
                "competitors_list": competitors_list, }

    return render (request, "adminPage.html", context)