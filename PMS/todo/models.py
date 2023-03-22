from django.db import models
# from user import models


# # Create your models here.
# # ------------------ PMS Tables ------------------------------
class Role(models.Model):
    role_name = models.CharField(max_length=25,unique=True,null=False)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'role'


technology_choices = (('DJANGO' , 'Django'), ('MERN', 'MERN'), ('MEAN', 'MEAN'))
class Project(models.Model):
    title = models.CharField(max_length=30,null=False)
    description = models.TextField()
    technology = models.CharField(null=True, choices = technology_choices , max_length=30)
    estimated_hours = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'


class Project_team(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    # user = models.ForeignKey(models.User,on_delete=models.CASCADE)   # ------------

    def __str__(self):
        return self.project

    class Meta:
        db_table = 'project_team'


class Status(models.Model):
    status_name = models.CharField(max_length=60,null=False,unique=True)

    def __str__(self):
        return self.status_name

    class Meta:
        db_table = 'status'


class Project_module(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    module_name = models.CharField(max_length=30,null=False)
    description= models.CharField(max_length=30)
    estimated_hours = models.IntegerField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return self.module_name

    class Meta:
        db_table = 'project_module'


class Task(models.Model):
    project_module = models.ForeignKey(Project_module,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=30,null=False)
    priority = models.CharField(max_length=30)
    description = models.TextField(null=False)
    status = models.ForeignKey(Status,on_delete=models.CASCADE) 
    totalminutes = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'


class User_task(models.Model):
    # user = models.ForeignKey(models.User,on_delete=models.CASCADE)   # -----------
    task = models.ForeignKey(Task,on_delete=models.CASCADE)

    def __str__(self):
        return self.task

    class Meta:
        db_table = 'user_task'
