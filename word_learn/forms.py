from django.contrib.auth import forms as auth_forms
from .models import Word
from django import forms


class WordForm(forms.ModelForm):
    '''
    英単語と日本語訳を登録するフォーム
    '''

    class Meta:
        model = Word
        fields = ('english_word', 'japanese_word')

        
#ブログ引用
class LoginForm(auth_forms.AuthenticationForm):
    '''
    ログインフォーム
    '''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label


