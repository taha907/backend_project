from django import forms
from django.forms import SelectMultiple, TextInput
from django.forms import Textarea
from .models import Course

"""
class CourseCreateForm(forms.Form):
    title = forms.CharField(label="kurs başlığı",required=True,error_messages={"required":"kurs başlığını girmediniz !"})
    description = forms.CharField(widget=forms.Textarea)
    imageUrl = forms.CharField()
    slug = forms.CharField()
"""

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields ={'title','description','image','slug','categories'}
        labels = {
            "title":"kurs başlığı",
            "description":"açıklama"
        }
        widgets={
            #burda htlm de default olarak gelen widgetlerin kontrolünü djangoya bootstrap ermek için classla atadık.
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
            
            }
        error_messages={
            "title": {"required":" kursbaşlığınmı girmelisinz",
                      "max_length":"maksimum 50 karakter girebilrisiniz"},
                      "description":{"required":"kurs açıklaması gereklidir."}
        }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields ={'title','description','image','slug','categories','isActive'}
        labels = {
            "title":"kurs başlığı",
            "description":"açıklama"
            
        }
        widgets={
            #burda htlm de default olarak gelen widgetlerin kontrolünü djangoya bootstrap ermek için classla atadık.
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "imageUrl":TextInput(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
            "categories":SelectMultiple(attrs={"class":"form-control"}),            
            }
        error_messages={
            "title": {"required":" kursbaşlığınmı girmelisinz",
                      "max_length":"maksimum 50 karakter girebilrisiniz"},
                      "description":{"required":"kurs açıklaması gereklidir."}
        }

    
