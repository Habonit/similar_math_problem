from django.db import models

class Chapter(models.Model):
    id = models.AutoField(primary_key=True)
    학교 = models.CharField(max_length=50)
    학년 = models.IntegerField()
    대단원명 = models.CharField(max_length=255)
    소단원명 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.학교} - {self.대단원명} - {self.소단원명}'
    
class Problem(models.Model): 
    id = models.AutoField(primary_key=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)  
    문제_경로 = models.CharField(max_length=255)
    해설_경로 = models.CharField(max_length=255)
    난이도 = models.IntegerField()
    문서_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id} - {self.chapter.id}'