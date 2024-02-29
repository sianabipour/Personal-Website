from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce import models as tinymce_models

class About(models.Model):
    title = models.CharField(_("title"), max_length=50)
    about = tinymce_models.HTMLField(_("about"))
    def __str__(self):
        return self.title
    

class Skill(models.Model):
    SKILL_OPTIONS =(
        ("PL","Programming Lanuages"),
        ("LB","Libraries Backend"),
        ("FD","Frontend Dev"),
        ("LF","Libraries Frontend"),
        ("DB","Database"),
        ("TOOL","Tools"),
        ("DP","Document")
        
    )
    
    category = models.CharField(max_length=100,choices=SKILL_OPTIONS,default="PL")
    title= models.CharField(max_length=100)
    rate= models.CharField(max_length=100)
    percentage= models.IntegerField()
    color= models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    skill = models.CharField(max_length=100)
    location= models.CharField(max_length=50,blank=True,null=True)
    link = models.URLField(blank=True,null=True)
    sdate = models.CharField(max_length=50)
    edate = models.CharField(max_length=50)
    description  = tinymce_models.HTMLField()
    
    def __str__(self):
        return self.skill
    
class Comment(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    text = models.TextField()
    published = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class Education(models.Model):

    certificate = models.CharField(max_length=60)
    location= models.CharField(max_length=60)
    sdate = models.CharField(max_length=60)
    edate = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.certificate
    
class Portfoilio(models.Model):
    
    reverse = models.BooleanField()
    name = models.CharField(_("name"), max_length=50)
    description = tinymce_models.HTMLField(_("description"))
    skills = models.CharField(_("skills"),max_length = 100) 
    site_name = models.URLField(_("site_name"), max_length=200)
    image = models.ImageField(_("image"), upload_to='Portfolio' , blank=True, null=True)
    def __str__(self):
        return self.name
    
    


class Tag(models.Model):
    name = models.CharField(_("name"), max_length=150)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return f'{self.name}'
    