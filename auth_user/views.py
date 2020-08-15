from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth


@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)

    return render(request,'top.html',{'user': user})
