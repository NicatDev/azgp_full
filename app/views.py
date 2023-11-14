from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from app.models import *
from django.db.models import Q,F,FloatField,Count
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count
from django.conf import settings
from django.db.models import F
import json
from django.urls import translate_url
from app.forms import Messageform
from django.contrib.auth import get_user_model
from django.http import JsonResponse
User = get_user_model()



def set_language(request, lang_code):
    url = request.META.get("HTTP_REFERER", None)
    if lang_code == 'az':
        return HttpResponseRedirect('/')
    else:
        response = redirect(translate_url(url, lang_code))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response
    
def create_shared_dictionary(url):
    

    if "/en/" in url:
        
        your_dict = {'home': 'Home', 'articles': 'Articles','contact':'Contact','portfolio':'Portfolio','services':'Services','about':'About','serviceTitle':'We are at your service with our own quality.','devices':'Devices that meet high standards.',
                     'blogtitle':'Learn more, stay tuned with us for the pulse of technology!','learn':'Learn more','partners':'Partners'}
    else:
        your_dict = {'home': 'Ana Səhifə', 'articles': 'Məqalələr','contact':'Əlaqə','portfolio':'Portfolia','services':'Xidmətlərimiz','about':'Haqqımızda','serviceTitle':'Artıq illərdiki, öz keyfiyyətimizlə sizlərin xidmətinizdəyik.','devices':'Yüksək standartlara cavab verən cihazlar',
                     'blogtitle':'Daha çox öyrən, bizimlə texnologiyanın nəbzini tut !','learn':'Daha ətraflı','partners':'Tərəfdaşlarımız'}
    return your_dict

def home(request):

    if HomeAbout.objects.exists():
        about = HomeAbout.objects.first()
    partners = Partners.objects.all()
    equips = Equipment.objects.all()
    services = Services.objects.all()
    portfolio = Portfolia.objects.all()
    blogs = Blog.objects.all()
    header = HeaderSlide.objects.all()
    context = {
        'about':about,
        'partners':partners,
        'equips':equips,
        'services':services,
        'portfolio':portfolio,
        'blogs':blogs,
        'headers':header
  
    }
    current_path = request.path
    nav = create_shared_dictionary(current_path)
    context['nav']=nav
    return render(request,'index.html',context)

def blog(request):
    bloglist = Blog.objects.all()
    category = request.GET.get('movzu')
    if category:
        bloglist = bloglist.filter(category__name=category)

    if request.GET.get('title'):
        name = request.GET.get('title')
        bloglist = bloglist.filter(Q(title__icontains=name) | Q(description__icontains=name) | Q(description2__icontains=name) | Q(minititle__icontains=name))
    paginator = Paginator(bloglist, 12)
    page = request.GET.get("page", 1)
    blogs = paginator.get_page(page)
    categories = Category.objects.all()
    page_count = paginator.num_pages
    count = [count for count in range(page_count)]
    recent_blogs = Blog.objects.all()
    if len(recent_blogs)>3:
        recent_blogs = recent_blogs[3]
    context = {
        'categories':categories,
        'blogs':blogs,
        'count':count,
        'recent_blogs':recent_blogs
    }
    current_path = request.path
    nav = create_shared_dictionary(current_path)
    context['nav']=nav
    return render(request,'blog.html',context)

def blogsingle(request,slug=None):
    categories = Category.objects.all()
    if slug:
        blog = Blog.objects.get(slug=slug)
    recent_blogs = Blog.objects.all()
    if len(recent_blogs)>3:
        recent_blogs = recent_blogs.filter(id!=blog.id)[3]
    context = {
        'blog':blog,
        'categories':categories,
        'recent_blogs':recent_blogs
    }
    current_path = request.path
    nav = create_shared_dictionary(current_path)
    context['nav']=nav
    return render(request,'blog-details.html',context)

def portfolio(request,slug=None):
    portfolio = Portfolia.objects.all()
    fields = Field.objects.all()
    context = {
        'portfolio':portfolio,
        'fields':fields
    }
    current_path = request.path
    nav = create_shared_dictionary(current_path)
    context['nav']=nav
    return render(request,'portfolio.html',context)



def portfoliosingle(request,slug=None):
    fields = Field.objects.all()
    if slug:
        Work = Portfolia.objects.get(slug=slug)
    recent_works = Portfolia.objects.all()
    if len(recent_works) >3:
        recent_works = recent_works[3]
    context = {
        'work':Work,
        'fields':fields,
        'recent_works':recent_works
    }
    current_path = request.path
    nav = create_shared_dictionary(current_path)
    context['nav']=nav
    return render(request,'portfolio-details.html',context)


def services(request):
    services = Services.objects.all()
    blogs = Blog.objects.all()
    if len(blogs)>3:
        blogs=blogs[3]
    context = {
        'services':services,
        'blogs':blogs
    }
    current_path = request.path
    nav = create_shared_dictionary(current_path)
    context['nav']=nav
    return render(request,'services.html',context)

def servicesingle(request,slug=None):
    if slug:
        service = Services.objects.get(slug=slug)
        services = Services.objects.all()
        if len(services)>4:
            services = services[4]
    context = {
        'service':service,
        'services':services
    }
    current_path = request.path
    nav = create_shared_dictionary(current_path)
    context['nav']=nav
    return render(request,'services-details.html',context)

def contact(request):

    context = {

    }
    current_path = request.path
    nav = create_shared_dictionary(current_path)
    context['nav']=nav
    return render(request,'contact.html',context)

def about(request):
    about = {}
    if About.objects.exists():
        about = About.objects.first()
    context = {
        'about':about
    }
    current_path = request.path
    nav = create_shared_dictionary(current_path)
    context['nav']=nav
    return render(request,'about.html',context)

def message(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        newmessage = Messageform(data=data)
        if data.get('message') == '':
            return HttpResponse(status=401)
    
        if data.get('name') == '':
            return HttpResponse(status=404)
        if data.get('email') == '':
            return HttpResponse(status=405)
        if newmessage.is_valid():
            newmessage.save()
        else:
            return HttpResponse(status=405) 
        data = {'message': 'Data saved successfully'}
        return JsonResponse(data)
    else:
        return HttpResponse(status=405) 