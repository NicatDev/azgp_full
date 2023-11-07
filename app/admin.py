from django.contrib import admin
from app.models import HomeAbout,Partners,Equipment,Services,Portfolia,Blog,Category,Field,About,Message,HeaderSlide
# Register your models here.
class HomeAboutAdmin(admin.ModelAdmin):
    exclude = ('title','description')
class BlogAdmin(admin.ModelAdmin):
    exclude = ('title','description','description2','minititle')
class PortAdmin(admin.ModelAdmin):
    exclude = ('title','description','description2','minititle','strong_description')
class NameAdmin(admin.ModelAdmin):
    exclude = ('name',)
admin.site.register(HomeAbout,HomeAboutAdmin)
admin.site.register(About,HomeAboutAdmin)
admin.site.register(Partners)
admin.site.register(Equipment)
admin.site.register(Services,BlogAdmin)
admin.site.register(Portfolia,PortAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,NameAdmin)
admin.site.register(Field,NameAdmin)
admin.site.register(Message)
admin.site.register(HeaderSlide)
