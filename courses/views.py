from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from datetime import date
from .models import Course, Category
from django.core.paginator import Paginator
from courses.forms import CourseCreateForm



#her django view fonksiyonu zorunlu olarak request parameteresi alır.
def index(request):
    kategoriler = Category.objects.all()
    kurslar = Course.objects.filter(isActive=1,isHome=True)

    #html'ye liste şeklinde action'dan 3. parametre kullanarak veri yolladık -> categories değişkeni ile
    # render(request, template, context)  context, view’dan template’e gönderilen değişkenlerin saklandığı sözlüktür.
    return render(request,'courses/index.html',{'categories': kategoriler,
                                                'courses':kurslar})

# GET  FORM
def search(request):
    if "q" in request.GET and request.GET["q"]!="":
        q = request.GET["q"]
        kategoriler = Category.objects.all()
        kurslar = Course.objects.filter(isActive=True,title__contains=q)
        #sayfa kaçar kaçar objelere bölünsün
    else:
        redirect("/kurslar")  

    return render(request,'courses/index.html',{
        'categories':kategoriler,
        'courses':kurslar
    })

def create_course(request):
    #FORM CLASS ile POST formunun kontrolü ve kaydedilmesi

    if request.method == "POST":
        form = CourseCreateForm(request.POST)

        # form.is_valid() FORM CLASS aracılığıyla gelen
        if form.is_valid():
            kurs = Course(title=form.cleaned_data["title"],
                          description=form.cleaned_data["description"],
                          imageUrl=form.cleaned_data["imageUrl"],
                          slug=form.cleaned_data["slug"])
            kurs.save()
            return redirect("/kurslar")
    form = CourseCreateForm()
    """
    *AÇIKLAMA 
    Form Class oluşturmadan Formdan gelen verileri alarak manuel hata kontrolü de yapıp veri tabanına kaydetme kodudur aşağıdaki
    if request.method =="POST":
        title = request.POST["title"]
        description = request.POST["description"]
        imageUrl=request.POST["imageUrl"]
        slug=request.POST["slug"]
        isActive= request.POST.get("isActive",False)
        isHome=request.POST.get("isHome",False)

        if isActive=="on":
            isActive=True
        if isHome=="on":
            isHome=True

        error = False
        msg = ""
        
        if title == "":
            error = True
            msg += "Title bilgisini Giriniz. "

        if len(title) < 5 and error==False:
            error = True
            msg += "Title bilgisi için daha uzun bir değer giriniz !"
 
       if error:
            return render(request,'courses/create-course.html',{'error':True, 'msg':msg})
        kurs = Course(title=title,description=description,imageUrl=imageUrl,slug=slug,isActive=isActive,isHome=isHome)
        kurs.save()
        return redirect("/kurslar")   
    """
     
    return render(request,'courses/create-course.html',{"form" : form})
     
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
    kurslar = Course.objects.filter(categories__slug = slug, isActive=True)
    #sayfa kaçar kaçar objelere bölünsün
    paginator = Paginator(kurslar,3)
    #2. 3. sayfalarda kaçar olsun? gelen isteği al,yoksa default=1 olsun
    page = request.GET.get('page',1)
    #kurslarıb son halini page olarak al
    page_obj = paginator.page(page)

    return render(request,'courses/list.html',{
        'categories':kategoriler,
        'page_obj':page_obj,
        'seciliKategori': slug
    })