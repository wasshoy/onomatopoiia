from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

from .models import Odai,Answer

def index(request):
    latest_answer=Answer.objects.order_by('-pub_date')[:3]
    context = {
        'latest_answer': latest_answer,
    }
    return render(request, 'onomato/index.html', context)

    # output =', \n'.join([q.odai for q in latest_answer])
    # return HttpResponse(output)

def odai_index(request):
    latest_odai=Odai.objects.order_by('-pub_date')[:3]
    context={'latest_odai': latest_odai}
    return render(request, 'onomato/odai_index.html', context)


def odai_detail(request, odai_id):
    odai=Odai.objects.get(id=odai_id)
    # 回答も取得
    # answers=Odai.
    return render(request, 'onomato/odai_detail.html',{'odai': odai}) #回答も渡す
