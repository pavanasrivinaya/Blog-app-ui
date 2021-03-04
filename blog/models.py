from django.db import models
from django.utils import timezone

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('VueJs', 'VueJs'),
        ('HTML','HTML'),
        ('CSS','CSS'),
        ('Machine learning','Machine learning'),
        ('JavaScript', 'JavaScript'),
        ('Jquery','Jquery'),
        ('Mongo DB','Mongo DB'),
        ('MySQL','MySQL'),


    )
    cover = models.FileField(default='')
    cover_2 = models.FileField(default='', null = True, blank = True)
    author = models.CharField(max_length=2000, default='')
    title = models.CharField(max_length=2000, default='')
    slug = models.SlugField(default='')
    text = models.TextField(default='')
    text_2 = models.TextField(default='')
    l_heading = models.CharField(max_length=2000, default='')
    l_heading_text = models.CharField(max_length=2000, default='')
    s_heading = models.CharField(max_length=2000, default='')
    s_heading_text = models.CharField(max_length=2000, default='')
    category = models.CharField(max_length=2000, choices=CATEGORY_CHOICES, default='')
    created_date = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    
    tag_1 = models.CharField(max_length=2000, default='')
    tag_2 = models.CharField(max_length=2000, default='')
    tag_3 = models.CharField(max_length=2000, default='')
     
    class Meta:
       ordering = ['-created_date']

    def __str__(self):
        return self.title
