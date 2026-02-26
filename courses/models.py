from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="",null=False,db_index=True,unique=True)

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50,blank=False)
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField()
    slug = models.SlugField(default="",null=False, unique=True, db_index=True)
    category=models.ForeignKey(Category,default=1,on_delete=models.CASCADE,related_name="kurslar")
    
    # many-to-one ilişkisi course-category(her kurs bağlı olduğu kategori idsini FK olarak sütununda tutar.
    # CASCADE -> Eğer bir kategori silinirse kategoriye bağlı olan tüm kurslarda veri tabanından silinsin
    # Önceden varolan kayıtlar için seçenekler: 
    # 1) veri tabanını sil ve tekrar migrate et
    # 2) default="1" gibi değer girerek tüm kurları otomatik var olan bir kategoriye bağla 
    # related_name --> sorgu yaparken (course__category) e denktir.
    
    
