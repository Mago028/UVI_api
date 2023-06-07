# models.py

from django.db import models

class UVI(models.Model):
    areaNo = models.CharField(max_length=255)
    
    def __str__(self):
        return self.areaNo
    # time = models.DateTimeField(auto_now=True)
    # 다른 필드들을 정의합니다.