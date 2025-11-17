from django.db import models
from django.utils.text import slugify

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50,blank=False)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default="",null=False, unique=True, db_index=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)
        #“Her .save() çağrıldığında, başlıktan otomatik olarak slug üret ve veritabanına o şekilde kaydet.”

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=40)