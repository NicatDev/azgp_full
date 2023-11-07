from modeltranslation.translator import TranslationOptions,register, translator
from app.models import *


class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    

class BlogTranslationOptions(TranslationOptions):
    fields = ('title','description','description2','minititle')

class PortTranslationOptions(TranslationOptions):
    fields = ('title','description','description2','minititle','strong_description')  
  
translator.register(About, AboutTranslationOptions)
translator.register(HomeAbout, AboutTranslationOptions)
translator.register(Field, CategoryTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Blog, BlogTranslationOptions)
translator.register(Equipment, AboutTranslationOptions)
translator.register(Services, BlogTranslationOptions)
translator.register(Portfolia, PortTranslationOptions)

