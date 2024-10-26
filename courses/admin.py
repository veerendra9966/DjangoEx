from django.contrib import admin
from .models import Course, Category

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'author_name')
    filter_horizontal = ('categories',)  
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)

 