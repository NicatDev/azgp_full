from django.db import models
from django.contrib.auth import get_user, get_user_model
from datetime import datetime
from django.utils.text import slugify

class BaseMixin(models.Model):
    slug = models.SlugField(unique=True,editable=False,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True,blank=True,null=True,)

    class Meta:
        abstract = True

class HeaderSlide(models.Model):
    minititle = models.CharField(max_length=330)
    title = models.CharField(max_length=340)
    mainimage = models.ImageField()
    name = models.CharField(max_length=500)
    icon = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.title + '---'
    

    
class HomeAbout(models.Model):
    project_done = models.SmallIntegerField(null=True,blank=True)
    happy_customer = models.SmallIntegerField(null=True,blank=True)
    image = models.ImageField()
    title = models.CharField(max_length=440)
    description = models.TextField(max_length=400)
    def __str__(self):
        return self.title + '---'

class About(models.Model):
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)
    title = models.CharField(max_length=440)
    description = models.TextField(max_length=400)
    vision = models.TextField(null=True)
    mission = models.TextField(null=True)
    projects = models.TextField(null=True)
    
    def __str__(self):
        return self.title + '---'

    
    def save(self, *args, **kwargs):
        self.pk = 1
        super(About, self).save(*args, **kwargs)  
        
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + '---'

        
class Blog(BaseMixin):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='blogs')
    minititle = models.CharField(max_length=300, blank=True, null=True)
    title = models.CharField(max_length=1200)
    description = models.TextField()
    description2 = models.TextField()
    views = models.SmallIntegerField(default=0)
    image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.title + '---'

    
    def save(self, *args, **kwargs):
        new_slug = slugify(self.title)
        self.slug = new_slug
        if Blog.objects.filter(slug=new_slug).exists():
            count = 1
            while Blog.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.title)}-{count}"
                count += 1
            self.slug = new_slug
        super(Blog, self).save(*args, **kwargs)  
        

class Partners(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    
    def __str__(self):
        return self.title + '---'

    
class Message(models.Model):
    name = models.CharField(max_length=600)
    message = models.TextField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name + '---'

    
class Contact(models.Model):
    address = models.CharField(max_length=400)
    contact = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    
    def __str__(self):
        return 'Contact'
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super(Contact, self).save(*args, **kwargs)

class Equipment(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField()
    field = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.title + '---'


        
class Services(BaseMixin):
    minititle = models.CharField(max_length=330)
    title = models.CharField(max_length=340)
    mainimage = models.ImageField()
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=500)
    description = models.TextField()
    description2 = models.TextField()
    icon = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.title + '---'

    
    def save(self, *args, **kwargs):
        new_slug = slugify(self.title)
        self.slug = new_slug
        if Services.objects.filter(slug=new_slug).exists():
            count = 1
            while Services.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.title)}-{count}"
                count += 1
            self.slug = new_slug
        super(Services, self).save(*args, **kwargs)  

class Field(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + '--- portfolia gorulen islerin sahesi filterlemek ucun'

class Portfolia(BaseMixin):
    minititle = models.CharField(max_length=330)
    title = models.CharField(max_length=340)
    mainimage = models.ImageField()
    name = models.CharField(max_length=500)
    description = models.TextField()
    strong_description = models.TextField(null=True,blank=True)
    description2 = models.TextField()
    icon = models.FileField(null=True,blank=True)
    field = models.ForeignKey(Field,on_delete=models.CASCADE,null=True)
    value = models.SmallIntegerField(null=True,blank=True)
    client_country = models.CharField(max_length=400,null=True,blank=True)
    
    def __str__(self):
        return self.title + '--- gorduyun isler'
 
    def save(self, *args, **kwargs):
        new_slug = slugify(self.title)
        self.slug = new_slug
        if Portfolia.objects.filter(slug=new_slug).exists():
            count = 1
            while Portfolia.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.title)}-{count}"
                count += 1
            self.slug = new_slug
        super(Portfolia, self).save(*args, **kwargs)  