
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('<kurs_id>',views.details),
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>',views.getCoursesByCategory, name ='courses_by_category')
    #name parametresi -> Kodda URL’yi doğrudan string olarak yazmak yerine bu ismi kullanmaktır.
    #Name Path --> Proje büyüdüğünde URL bilgilerini tek tek yazmak ve karışıklığı önlemek amacıyla kullanılır
] 