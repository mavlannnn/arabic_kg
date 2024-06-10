from django.db import models


class Translation(models.Model):
    arabic_word = models.CharField(max_length=255)
    kyrgyz_word = models.CharField(max_length=255)
    meaning = models.TextField()

    def __str__(self):
        return f'{self.arabic_word} - {self.kyrgyz_word}'


