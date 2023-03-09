from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from ..forms.Forms import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from ..models import *



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
    fields = ['title', 'subtitle', 'text', 'datetime', 'category']