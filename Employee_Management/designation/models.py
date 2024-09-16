from django.db import models

class Designation(models.Model):
    title = models.CharField(max_length=50) #এটির ডাটা Backend এ (admin panel) এন্ট্রি দিতে হবে।

    def __str__(self):
        return self.title
    
    
    