from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer_text',)
        labels = {'answer_text': 'これはなに？'}


# ↓ 岩崎くんのコード。一旦コメントアウト。
# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = ('answer_text',)
#         # TODO: 回答のユーザー情報を追加

# TODO: 試しコード。いらなくなったら消す。
# class AnswerForm(forms.Form):
# #    odai = forms.CharField()
#    answer_text = forms.CharField()
