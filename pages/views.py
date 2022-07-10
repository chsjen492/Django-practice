from django.shortcuts import render


# 메인 페이지
def mainpage(request):
    return render(request, 'pages/mainpage.html')

# 회사소개 페이지
def company(request):
    return render(request, 'pages/company_info.html')
