from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from datetime import date
from .models import Course, Category



#her django view fonksiyonu zorunlu olarak request parameteresi alır.
def index(request):
    kategoriler = Category.objects.all()
    kurslar = Course.objects.filter(isActive=1)

    #html'ye liste şeklinde action'dan 3. parametre kullanarak veri yolladık -> categories değişkeni ile
    # render(request, template, context)  context, view’dan template’e gönderilen değişkenlerin saklandığı sözlüktür.
    return render(request,'courses/index.html',{'categories': kategoriler,
                                                'courses':kurslar})


def details(request,slug):
    try:
        course = Course.objects.get(slug=slug)
    except:
        raise Http404()
    
    context = {
    'course':course
    }
    return render(request,'courses/details.html',context)

def getCoursesByCategory(request,slug):
    kategoriler = Category.objects.all()
    kurslar = Course.objects.filter(category__slug = slug, isActive=True)

    return render(request,'courses/index.html',{
        'categories':kategoriler,
        'courses':kurslar,
        'seciliKategori': slug
    })