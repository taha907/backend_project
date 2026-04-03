from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Githubdan yorum saıtını düzenledim.
urlpatterns = [
    path('', include('pages.urls')),
    path('kurslar/',include('courses.urls')),
    path('account/',include('account.urls')),
    path('admin/', admin.site.urls),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# Normalde django web sunucusu değildir.
# static(...) Fonksiyonu: Django'nun urls.py dosyasını bir "dosya sunucusuna" dönüştüren yardımcı bir araçtır.
# Eğer birisi /media/ ile başlayan bir dosya isterse, git benim MEDIA_ROOT klasörüme bak ve o dosyayı ona gönder.
# Django'nun urls.py dosyasını bir "dosya sunucusuna" dönüştüren yardımcı bir araçtır. 

