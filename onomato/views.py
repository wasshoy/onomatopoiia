from django.shortcuts import render
from django.views.generic.edit import FormView,CreateView
from .models import Odai,Answer
from .forms import AnswerForm
def index(request):
    latest_answer = Answer.objects.order_by('-pub_date')[:3]
    context = {
        'latest_answer': latest_answer,
    }
    return render(request, 'onomato/index.html', context)
    
def odai_index(request):
    latest_odai = Odai.objects.order_by('-pub_date')[:3]
    context = {'latest_odai': latest_odai}
    print(context)
    return render(request, 'onomato/odai.html', context)


def odai_detail(request, odai_id):
    odai = Odai.objects.get(id=odai_id)
    return render(request, 'onomato/odai_detail.html', {'odai': odai})


class AnswerCreateView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'onomato/odai_detail.html'
    fields = ['answer_text',]
    success_url = '/'