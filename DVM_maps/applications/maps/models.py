from django.db import models

# Create your models here.
class Project(models.Model):
    # Project information including default primary and secondary DVM servers
    name = models.CharField(verbose_name="Name", max_length=100)
    description = models.TextField(verbose_name="Description", max_length=500, blank=True, null=True)
    owner = models.CharField(verbose_name="Owner", max_length=100, default="*")
    primary_srv = models.CharField(verbose_name="DVM primary server", max_length=100)
    redundant_srv = models.CharField(verbose_name="DVM redundant server", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    
class Site(models.Model):
    # Sites (every web page with cameras and jumps to another site) information
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Name", max_length=50)
    description = models.TextField(verbose_name="Description", max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Camera(models.Model):
    # Camera information like name and X and Y position in the site web page
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Name", max_length=50)
    number = models.IntegerField()
    primary_srv = models.CharField(verbose_name="DVM primary server", max_length=100)
    redundant_srv = models.CharField(verbose_name="DVM redundant server", max_length=100, blank=True, null=True)
    pox = models.IntegerField()
    poy = models.IntegerField()

    def __str__(self):
        return self.name, self.number

class Jump(models.Model):
    # Links to another web page. It contains the X and Y position in the site web page
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Name", max_length=50)
    jump = models.CharField(verbose_name="Jump to page", max_length=255)
    pox = models.IntegerField()
    poy = models.IntegerField()

    def __str__(self):
        return self.jump

