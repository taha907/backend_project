import os
import random

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from datetime import date
from .models import Course, Category, UploadForm
from django.core.paginator import Paginator
from courses.forms import CourseCreateForm, CourseEditForm



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
        #Bu, formun veriye bağlı (bound) halidir.
        form = CourseCreateForm(request.POST,request.FILES)

        # form.is_valid() GEÇERLİ Mİ? FORM CLASS aracılığıyla gelen
        if form.is_valid():
            # form model sınıfı olarak course kullanıyor. course aynı zamanda bir model ve migrations yani veri tabani ile bağlantılı olduğundan form.save() kullanımı Course(veriler).save() ile aynıdır.
            form.save()
            return redirect("/kurslar")
    else:
        #Bu, formun boş (unbound) halidir.
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

def course_list(request):
    kurslar = Course.objects.all()
    return render(request,'courses/course-list.html',{'courses':kurslar})

def course_edit(request,id):
    course = get_object_or_404(Course,pk=id)

    #düzenleme bitip göndere basılırsa
    if request.method == "POST":
        #birinci parametre girilen input text bilgileri ile formu doldurur, ikinci parametre veritabanındaki kurs bilgisi
        form = CourseEditForm(request.POST,request.FILES,instance=course)
        form.save()
        return redirect("course_list")
    #sayaf ilk açıldığında düzenleme ekranında düzenşenecek eski bilgileri göster
    else:
        form = CourseEditForm(instance=course)
    return render(request,"courses/edit-course.html",{"form":form})

def course_delete(request,id):
    course = get_object_or_404(Course,pk=id)

    if request.method=="POST":
        Course.objects.get(pk=id).delete()
        return redirect('course_list')
 
    return render(request,"courses/delete-course.html",{"course":course})

def upload_image(request):
    """
 if request.method=="POST":
        #çoklu resim yüklemede bu yöntem kullanılır.
        uploaded_images = request.FILES.getlist('images')
        for image in uploaded_images:
            handle_uploaded_files(image)
        return render(request,'courses/succesfull-image.html')
 """ 
    if request.method == "POST":
        modelForm = UploadForm(image=request.FILES["image"])
        modelForm.save()
        return render(request,"courses/successful-image.html")
    else:
        modelForm = UploadForm()
    return render(request,'courses/upload-image.html')

  
def handle_uploaded_files(file):
    number = random.randint(1,99999)
    filename, file_extensions = os.path.splitext(file.name)
    name = filename + "_" + str(number) + file_extensions

    with open("temp/"+name,"wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

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