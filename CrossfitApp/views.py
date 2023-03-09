from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .forms.Forms import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import *


@login_required
def about_user(request): 
    return render(request, 'UserPage.html')

@login_required
def homePage(request): 
    user_data = User.objects.get(username = request.user)
    print(user_data.email)
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
    print(query)

    return render(request, "blog.html" ,{"blog_list": blog_list, "blog_types": blog_type})

@login_required
def blogDetail(request, pk):
    form = ReviewsBlogsForm(initial={"name": request.user}) 
    blog_detail = Blog.objects.filter(id = pk).first()
    review_from_blog = Review.objects.filter(Category = blog_detail)

    if request.method == "POST": 
        form = ReviewsBlogsForm(request.POST)
        if form.is_valid(): 
            form.save()
            return render(request, "blogDetail.html", {"blog": blog_detail, "reviews": review_from_blog, "form_review": form})
    return render(request, "blogDetail.html", {"blog": blog_detail, "reviews": review_from_blog, "form_review": form})


@login_required
def login_user(request): 
    return render(request, "loginpage.html")

def create_competition(request): 
    form = CreateCompetition()
    if request.method == 'POST': 
        form = CreateCompetition(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("adminpage")
        else: 
            return render(request, "createCompetition.html", {"form": form, "message":"Invalidad data types, please check..."})
    else: 
        return render(request, "createCompetition.html", {"form": form})


@login_required
def competition_detail(request, pk): 
    form_competitionEnroll = CompetitionEnrollForm(initial={"user_linked": request.user})
    competition = Competition.objects.filter(id = pk).first()
    competitors = Competitors.objects.filter(competition_in=competition)    

    is_in = False

    for competitor in competitors: 
        user_convert = str(request.user)
        if competitor.user_linked == user_convert: 
            is_in = True


    if is_in: 
        form_competitionEnroll = None



    if request.method == 'POST':         
        
        form_competitionEnroll = CompetitionEnrollForm(request.POST, request.FILES)
        if form_competitionEnroll.is_valid(): 
            form_competitionEnroll.save()
            # return render(request, "competitionDetail.html", {"competitors": competitors, "competition_detail": competition, "form": form_competitionEnroll}) 
            return redirect("competition")

    else:
         return render(request, "competitionDetail.html", {"competitors": competitors, "competition_detail": competition, "form": form_competitionEnroll}) 

    return render(request, "competitionDetail.html", {"competitors": competitors, "competition_detail": competition, "form": form_competitionEnroll})

@login_required
def admin_page(request): 
    competition_list = Competition.objects.all()
    competitors_list = Competitors.objects.all()
    review_list = Review.objects.all()
    blog_list = Blog.objects.all() 

    return render (request, "adminPage.html", 
                   {"competition_list": competition_list, "competitors_list": competitors_list, 
                    "review_list": review_list, "blog_list": blog_list})



@login_required
def update_user(request): 
    user = User.objects.get(username = request.user)
    
    competitors = Competitors.objects.all()


    if request.method == "POST": 
        form = UserEditForm(request.POST)
        if form.is_valid(): 
            info_user = form.cleaned_data
            user.username = info_user['username']
            user.first_name = info_user['first_name']
            user.last_name = info_user['last_name']
            user.email = info_user['email']
            user.save()
            
            return redirect("about")

    form = UserEditForm(
        initial=
        {"username": user.username, 
         "email": user.email, 
         "first_name": user.first_name, 
         "last_name": user.last_name
         })
    return render(request, 'UserEditFormPage.html', {"form": form})








class UpdateCompetition(UpdateView): 
    model = Competition
    template_name = 'CompetitionUpdate.html'
    success_url = reverse_lazy('adminpage')
    fields = ['name', 'category', 'state', 'country']

class UpdateBlog(UpdateView): 
    model = Blog
    template_name = 'updateBlog.html'
    success_url = reverse_lazy('adminpage')
    fields = ['title', 'subtitle', 'text']


class DeleteBlog(DeleteView): 
    model = Blog
    template_name = 'deleteBlog.html'
    success_url = reverse_lazy('adminpage')

class Out_Of_Competition(DeleteView): 
    model = Competitors
    template_name = 'OutOfCompetition.html'
    success_url = reverse_lazy('homepage')

class DeleteReview(DeleteView): 
    model = Review
    template_name = 'deleteReview.html'
    success_url = reverse_lazy('adminpage')


class DeleteCompetitor(DeleteView): 
    model = Competitors
    template_name = 'deleteCompetitor.html'
    success_url = reverse_lazy('adminpage')


class DeleteCompetition(DeleteView): 
    model = Competition
    template_name = 'deleteCompetition.html'
    success_url = reverse_lazy('adminpage')

class CreateBlog(CreateView): 
    model = Blog
    template_name = 'createBlog.html'
    success_url = reverse_lazy('adminpage')
    fields = ['title', 'subtitle', 'text', 'category']


