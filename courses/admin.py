from django.contrib import admin
from .models import Course,Category


#Modellerin admin panele eklenmesi ve özelleştirilmesi

# Register your models here
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","slug","course_count")
    prepopulated_fields={"slug":("name",),}

    def course_count(self,obj):
        return obj.course_set.count()

    

#modelleri özelleştirebiliriz
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): 
    list_display=("title","isActive","slug","category_list")
    search_fields=("title",)
    # readonly_fields=("slug",)
    prepopulated_fields={"slug":("title",),}
    list_filter=("title","isActive")
    list_editable=("isActive",)

    

    #burdaki obj bilgisi o an hangi category objesi için çalışıyorsa onu atar
    def category_list(self,obj):
        html=""
        for category in obj.categories.all():
            html+= category.name + " "
        return html
        