from django import forms
from .models import Answer
# from django.forms import ModelForm

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer_text',)
# #         # ユーザー情報をのちに追加

# class AnswerForm(forms.Form):
# #    odai = forms.CharField()
#    answer_text = forms.CharField()