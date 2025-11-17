from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from datetime import date
from .models import Course, Category

data = {"programlama":"programlama kategorisine ait kurslar",
        "web-gelistirme":"web-geliştirme kategorisine ait kurslar",
        "mobil-uygulama":"mobil geliştirme kategorisine ait kurslar"
}

db = {
    "courses": [
        {
            "title":"javascript kursu",
            "description":"javascript kursunun açıklamasıdır.",
            "imageUrl":"1.png",
            "slug":"javascript-kursu",
            "date": date(2022,10,10),
            "isActive":True
        },
         {
            "title":"python kursu",
            "description":"python kursunun açıklamasıdır.",
            "imageUrl":"2.jpg",
            "slug":"python-kursu",
            "date": date(2023,10,10),
            "isActive":True
        },
        {
            "title":"web geliştirme kursu",
            "description":"web kursunun açıklamasıdır.",
            "imageUrl":"3.jpg",
            "slug":"web-geliştirme",
            "date": date(2024,10,10),
            "isActive":True
        }],
    "categories" : [
        {"id":1, "name":"programlama","slug":"programlama"},
        {"id":2, "name":"web geliştirme","slug":"web-gelistirme"},
        {"id":3, "name":"mobil uygulama","slug":"mobil-uygulama"}]
}
#her django view fonksiyonu zorunlu olarak request parameteresi alır.
def index(request):
    kategoriler = Category.objects.all()
    kurslar = Course.objects.filter(isActive=1)

            
    
    #html'ye liste şeklinde action'dan 3. parametre kullanarak veri yolladık -> categories değişkeni ile
    # render(request, template, context)  context, view’dan template’e gönderilen değişkenlerin saklandığı sözlüktür.
    return render(request,'courses/index.html',{'categories': kategoriler,
                                                'courses':kurslar})


def details(request,kurs_id):
    try:
        course = Course.objects.get(pk=kurs_id)
       
    except:
        raise Http404()
    context = {
    'course':course
    }
    return render(request,'courses/details.html',context)

def getCoursesByCategory(request,category_name):
    try:    
        category_text = data[category_name]
        return render(request,"courses/kurslar.html",{
            'category':category_name,
            'category_text':category_text
        })
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")

def getCoursesByCategoryId(request,category_id):
    category_list = list(data.keys())
    if(category_id>len(data)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    
    category = category_list[category_id - 1]

    # url patternin nameini yeniden yepılandırır, args-> dinamik kısımları sırayla atar
    redirect_url = reverse('courses_by_category',args=[category])
    
    return redirect(redirect_url)