from django.db import models
from django.shortcuts import reverse

    
class Blog(models.Model):
    header = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.DateField()
    text = models.TextField()
    instagram = models.TextField()
    twitter = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to="blog/")
    
    def __str__(self):
        return self.header
    
    def get_absolute_url(self):
        return reverse('blog', kwargs=[self.slug])
    
class Comment(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    date = models.DateField(auto_now_add=True)
    comment = models.TextField()
    image = models.ImageField(upload_to="blog/",null=True,blank=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments",null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    




