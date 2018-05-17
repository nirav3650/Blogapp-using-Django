from django.shortcuts import render , redirect
from .models import Blogpost
from django.views.generic import ListView, DetailView
# Create your views here.


class Bloglist(ListView):
    context_object_name = 'blogpostfound'
    template_name = 'blogs1/blogpost.html'

    def get_queryset(self):
        return Blogpost.objects.all()


class Blogviews(DetailView):
    model = Blogpost
    template_name = 'blog1/blogdetails.html'

def add_data(request):
    return render(request , 'blog1/blogpostadd.html')

def post_new(request):
    if request.method == "POST":
        print("hi")
        cemetery = Blogpost()
        cemetery.blog_title = request.POST.get('uname')
        cemetery.blog_description = request.POST.get('esal')
        cemetery.save()

    return redirect('/')
