from django.db import models
from .managers import TodoManager

class Todo(models.Model):
    title = models.CharField(max_length=110, verbose_name='Title of Your Todo')
    user = models.ForeignKey(to='accounts.CustomUser',verbose_name='For User', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False, verbose_name='Is Done?')
    
    objects = TodoManager()
    class Meta:
        ordering =  ('-title',)
    
    def __str__(self):
        return f'todo: {self.title}'
