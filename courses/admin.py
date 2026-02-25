from django.contrib import admin
from .models import Course,Category


#Modellerin admin panele eklenmesi ve özelleştirilmesi

# Register your models here
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","slug")
    prepopulated_fields={"slug":("name",),}

#modelleri özelleştirebiliriz
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): 
    list_display=("title","isActive","slug")
    search_fields=("title",)
    # readonly_fields=("slug",)
    prepopulated_fields={"slug":("title",),}
    list_filter=("title","isActive")
    list_editable=("isActive",)
