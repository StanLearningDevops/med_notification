from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView
from .models import Data
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
class DataPageView(LoginRequiredMixin, ListView):
    model = Data
    template_name = 'data_list.html'
    login_url = 'login'
    
class DataCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    
    login_url = reverse_lazy('data_detail')
        
    model = Data
    template_name = 'data_new.html'
    fields = ('detail', 'patient')
    login_url= 'login'
    success_url = 'data_detail'
    
    
    def test_func(self):
        return self.request.user.is_admin
    
    def handle_no_permission(self):
        return redirect('data_detail')