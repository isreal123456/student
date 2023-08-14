# from django.shortcuts import render
# from django.views.generic import TemplateView, CreateView, DetailView, ListView
#
# from book.models import book
#
#
# # Create your views here.
# class HomePage(TemplateView):
#     template_name = "school/home.html"
#
#
# class createbook(CreateView):
#     template_name = "book/create.html"
#     model = book
#     context_object_name = book
#     fields = "__all__"
#
#
# class listbook(ListView):
#     template_name = "book/list.html"
#     model = book
#     context_object_name = "book"
#
#
# class detail(DetailView):
#     template_name = "book/detail.html"
#     model = book
#     context_object_name = "book"
