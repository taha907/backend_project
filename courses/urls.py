
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('<slug:slug>',views.details,name="course_details"),
    #path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<slug:slug>',views.getCoursesByCategory, name ='courses_by_category')
    #name parametresi -> Kodda URL’yi doğrudan string olarak yazmak yerine bu ismi kullanmaktır.
    #Name Path --> Proje büyüdüğünde URL bilgilerini tek tek yazmak ve karışıklığı önlemek amacıyla kullanılır
] 