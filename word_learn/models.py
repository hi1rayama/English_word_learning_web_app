from django.conf import settings
from django.db import models
from django.utils import timezone


class Word(models.Model):
    '''
    英単語を登録するモデル
    ユーザー、英単語、日本語訳、作成日時
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weak=models.BooleanField(default=False)
    english_word = models.CharField(null=False,max_length=200)
    japanese_word = models.CharField(null=False,max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.english_word

'''
class WeakList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word_number=models.OneToOneField(Word.id,on_delete=models.CASCADE,)
    english_word = models.CharField(null=False,max_length=200)
    japanese_word = models.CharField(null=False,max_length=200)

    def __str__(self):
        return self.english_word
'''









