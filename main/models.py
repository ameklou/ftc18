from django.db import models

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


class Project(models.Model):
    """
        FTC18 Participants projects
    """
    title=models.CharField(max_length=250)
    author=models.ForeignKey(Author, related_name='main_projects', on_delete=models.CASCADE)
    link=models.CharField(max_length=250)
    description=models.TextField()
    cover=models.ImageField(upload_to="covers")
