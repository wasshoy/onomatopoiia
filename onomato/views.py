from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Odai, Answer
from .forms import AnswerForm


def index(request):
    latest_answer = Answer.objects.order_by('-pub_date')[:3]
    context = {
        'latest_answer': latest_answer,
    }
    return render(request, 'onomato/index.html', context)


def odai_index(request):
    latest_odai = Odai.objects.order_by('-pub_date')
    context = {'latest_odai': latest_odai}
    return render(request, 'onomato/odai.html', context)


def about(request):
    return render(request, 'onomato/about.html')


def tos(request):
    return render(request, 'onomato/tos.html')


def odai_detail(request, odai_id):
    odai = Odai.objects.get(id=odai_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)  # フォームの内容を保存
            # フォームで入力された値以外を埋める
            answer.odai = odai
            answer.pub_date = timezone.now()
            answer.save()  # 再び保存
            # TODO: url の指定がハードコーディングなため、修正の必要がある
            # return redirect('odai_detail', {'odai_id': odai_id})   # この書き方だとエラー
            return redirect(f'/onomato/odai/{odai_id}')
    else:
        context = {'odai': odai}
        return render(request, 'onomato/odai_detail.html', context)


def answer_forms(request):
    print('forms のビュー')
    form = AnswerForm(request.GET or None)
    if form.is_valid():
        message = 'データ検証に成功しました。'
    else:
        message = 'データ検証に失敗しました。'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'onomato/forms.html', context)


# 岩崎くんのコード。一旦コメントアウト。
# class AnswerCreateView(generic.CreateView):
#     model = Answer
#     form_class = AnswerForm
#     template_name = 'onomato/odai_detail.html'
#     success_url = reverse_lazy('onomato:odai')
