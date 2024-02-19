from django.db import models

# Create your models here.

class ProjectManager(models.Model):
    name = models.CharField(max_length = 100,unique=True)
    created = models.DateTimeField(auto_now_add = True)
    modefied = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=299,unique=True)
    projectmanager=models.ForeignKey(ProjectManager,on_delete=models.CASCADE,null=True,blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.CharField(max_length=333)
    status = models.CharField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add = True)
    modefied = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    
