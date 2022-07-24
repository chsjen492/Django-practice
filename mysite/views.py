
from django.shortcuts import get_object_or_404, render
from .models import MainContent

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')  # 목록 출력, -를 붙여 날자 역순으로 출력됨
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)  # content_list를 html파일에 적용 후 리턴

def detail(request, content_id):

    content_list = get_object_or_404(MainContent, pk=content_id)
    context = {'content_list': content_list}
    return render(request, 'mysite/comtent_detail.html', context)