from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

data = {"programlama":"programlama kategorisine ait kurslar",
        "web-geliştirme":"web-geliştirme kategorisine ait kurslar",
        "mobil geliştirme ":"mobil  geliştirme kategorisine ait kurslar"
}
def index(request):
    return render(request,'courses/index.html')

def kurslar(request):
    return HttpResponse("Kurslar")

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

    redirect_url = reverse('courses_by_category',args=[category])
    
    return redirect(redirect_url)
    
