from django.db import models
from django.urls import reverse
# Create your models here.

class Author(models.Model):
    """
        FTC18 Participants profil
    """

    city_choices=(
    ('Lome','Lome'),
    ('Kara','Kara'),
    )
    name=models.CharField(max_length=250)
    profession=models.CharField(max_length=250)
    city=models.CharField(max_length=50,choices=city_choices)
    bio=models.TextField()
    picture=models.ImageField(upload_to="pictures")
    slug=models.SlugField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects_authors', args=[self.slug,self.id])


class Project(models.Model):
    """
        FTC18 Participants projects
    """
    title=models.CharField(max_length=250)
    author=models.ForeignKey(Author, related_name='main_projects', on_delete=models.CASCADE)
    link=models.CharField(max_length=250)
    description=models.TextField()
    cover=models.ImageField(upload_to="covers")
    slug=models.SlugField(max_length=250)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects', args=[self.slug,self.author])
