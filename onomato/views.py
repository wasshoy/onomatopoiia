from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone


from .models import Odai, Answer
from .forms import AnswerForm


def index(request):
    latest_answer = Answer.objects.order_by('-pub_date')[:5]
    context = {
        'latest_answer': latest_answer,
    }
    return render(request, 'index.html', context)


def odai_index(request):
    latest_odai = Odai.objects.order_by('-pub_date')
    context = {'latest_odai': latest_odai}
    return render(request, 'odai.html', context)


def about(request):
    return render(request, 'about.html')


def tos(request):
    return render(request, 'tos.html')


def contact(request):
    return render(request, 'contact.html')


def odai_detail(request, odai_id):
    odai = Odai.objects.get(id=odai_id)
    is_login = request.user.is_authenticated

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)  # フォームの内容を保存(DBには反映しない)
            # フォームで入力された値以外を埋める
            answer.odai = odai
            answer.pub_date = timezone.now()
            answer.save()  # 再び保存(DBに反映)
            # TODO: url の指定がハードコーディングなため、修正の必要がある
            # この書き方だとエラー
            # return redirect('odai_detail', {'odai_id': odai_id})
            return redirect(f'/odai/{odai_id}')
        else:
            form = AnswerForm()
            context = {'odai': odai, 'form': form, 'is_login': is_login}
            return render(request, 'odai_detail.html', context)

    else:
        context = {'odai': odai, 'is_login': is_login}
        return render(request, 'odai_detail.html', context)
