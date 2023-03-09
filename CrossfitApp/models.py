from django.db import models

class Blog_type(models.Model): 
    name = models.CharField(max_length=50)
    def __str__(self): 
        return self.name


class Blog(models.Model): 
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Blog_type, on_delete=models.CASCADE)
    def __str__(self): 
        return self.title 

class Review(models.Model):
    name = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=150)
    Category = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    def __str__(self): 
        return self.name + " " + self.text[0:20] + "..."


class Category(models.Model): 
    name = models.CharField(max_length=50)
    def __str__(self): 
        return self.name

class Competition(models.Model): 
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    def __str__(self): 
        return self.name 

class Competitors(models.Model): 
    competition_in = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='images/', null=True, blank=True)
    user_linked = models.CharField(max_length=40, null=True, blank=True)
    def __str__(self): 
        return self.name + " " + self.lastname
    
    class Meta: 
        unique_together = [["competition_in", "user_linked"]]
