from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from datetime import date

data = {"programlama":"programlama kategorisine ait kurslar",
        "web-geliştirme":"web-geliştirme kategorisine ait kurslar",
        "mobil-geliştirme":"mobil geliştirme kategorisine ait kurslar"
}

db = {
    "courses": [
        {
            "title":"javascript kursu",
            "description":"javascript kursunun açıklamasıdır.",
            "imageUrl":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuHnJDLOcdm_0b6N6kNj-1OvO9KhKYgqIy0w&s",
            "slug":"javascript-kursu",
            "date": date(2022,10,10),
            "is-active":True
        },
         {
            "title":"python kursu",
            "description":"python kursunun açıklamasıdır.",
            "imageUrl":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuHnJDLOcdm_0b6N6kNj-1OvO9KhKYgqIy0w&s",
            "slug":"python-kursu",
            "date": date(2023,10,10),
            "is-active":False
        },
        {
            "title":"web geliştirme kursu",
            "description":"web kursunun açıklamasıdır.",
            "imageUrl":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuHnJDLOcdm_0b6N6kNj-1OvO9KhKYgqIy0w&s",
            "slug":"web-geliştirme-kursu",
            "date": date(2024,10,10),
            "is-active":True
        }]
}

def index(request):
    category_list = list(data.keys())
    #html'ye liste şeklinde action'dan 3. parametre kullanarak veri yolladık -> categories değişkeni ile
    return render(request,'courses/index.html',{'categories': category_list})

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} kursunun detay sayfası")

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