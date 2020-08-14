from django.db import models


class Odai(models.Model):
    odai_text = models.CharField(max_length=4)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'<{self.odai_text}>'


class Answer(models.Model):
    odai = models.ForeignKey(Odai, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=50, null=False)
    pub_date = models.DateTimeField('date published')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # TODO: 回答のユーザー情報をログイン機能と共に追加

    def __str__(self):
        return f'<{self.odai.odai_text}:{self.answer_text}>'

# TODO: 試しコード？ 不要であれば消す。
# class User(models.Model):
#     user_name = models.CharField(max_length=10)
