from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    pst_title = models.CharField(max_length=40, verbose_name='Title')
    pst_image = models.ImageField(verbose_name='Image', upload_to='uploads')
    content = models.TextField(verbose_name='Details')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_date = models.TextField(verbose_name='Date e.g 20th, June 2022.')
    date = models.DateTimeField(verbose_name='Date', auto_now_add=True)
    
    def __str__(self):
        return self.pst_title
    
    class Meta():
        verbose_name_plural = 'Upcoming Events'
        
    def post_img(self):
        if self.pst_image:
            return self.pst_image.url
        