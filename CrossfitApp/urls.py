from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('Login.urls')), 
    path('', include('Register.urls')),
    
    path("", homePage, name="homepage"), 
    path("about",about_user, name="about"),
    path("user/edit", update_user, name="edituser"),

    path("competitions/", competition, name="competition"),  
    path("competitions/<pk>", competition_detail, name="competitionDetail"),
    path("competitions/competitor/delete/<pk>", Out_Of_Competition.as_view(), name="outcompetition"),
    
    path("blog/", blog, name="blog"), 
    path("blog/<pk>/", blogDetail, name="blogDetail"), 

    path("admin/", admin_page, name="adminpage"), 
    
    path("admin/blog/delete/<pk>", DeleteBlog.as_view(), name="deleteblog"), 
    path("admin/create/blog", CreateBlog.as_view(), name="createblog"),
    path("admin/blog/<pk>", UpdateBlog.as_view(), name="updateview"), 
    
    path("admin/competition/<pk>", UpdateCompetition.as_view(), name="updatecompetition"), 
    path("admin/competition/delete/<pk>", DeleteCompetition.as_view(), name="deletecompetition"), 
   
    path("admin/competitor/delete/<pk>", DeleteCompetitor.as_view(), name="deleteCompetitor"), 
    
    path("admin/review/delete/<pk>", DeleteReview.as_view(), name="deleteReview"), 
    
    path("admin/competiton/create/", create_competition, name="createcompetition"),
    ]