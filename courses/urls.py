
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('search',views.search, name="search"),
    path('create-course',views.create_course,name="create_course"),
    path('course-list',views.course_list,name="course_list"),
    path('course-edit/<int:id>',views.course_edit,name="course_edit"),
    path('course-delete/<int:id>',views.course_delete,name="course_delete"),
    path('upload-image',views.upload_image,name="upload_image"),
    path('<slug:slug>',views.details,name="course_details"),
    #path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<slug:slug>',views.getCoursesByCategory, name ='courses_by_category')
    # kategori sabittir. yakalanacak değişken tipi : yakalanacak değişkenin ismidir. 
    #name parametresi -> Kodda URL’yi doğrudan string olarak yazmak yerine bu ismi kullanmaktır.
    #Name Path --> Proje büyüdüğünde URL bilgilerini tek tek yazmak ve karışıklığı önlemek amacıyla kullanılır
]  