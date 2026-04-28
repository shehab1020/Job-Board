from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Job(models.Model):
    title = models.CharField(max_length=25)
    #location 
    x = [
        ('Full Time','Full Time'),
        ('part time','part time')
    ]
    user = models.ForeignKey(User, related_name="job_user", on_delete=models.CASCADE, blank=True, null=True)
    job_type = models.CharField(max_length=25, choices=x, blank=True, null=True) 
    description = models.CharField(max_length=400, blank=True, null=True)
    published_at = models.DateField(auto_now=True, blank=True, null=True)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    Vacancy = models.IntegerField( blank=True, null=True)
    experience = models.IntegerField( blank=True, null=True)
    image = models.ImageField(upload_to="jobs/%y/%m", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)



class Category(models.Model):
    name = models.CharField( max_length=50)


    def __str__(self):
        return self.name
    

class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to="apply/")
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.name



