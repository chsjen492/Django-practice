from django.shortcuts import render


# 메인 페이지
def mainpage(request):
    return render(request, 'mysite/content_list.html')

# 회사소개 페이지
def company(request):
    return render(request, 'pages/company_info.html')

# 서비스 페이지
def services(request):
    return render(request, 'pages/services.html')

# 홍보자료 페이지
def promotion(request):
    return render(request, 'pages/promotion.html')

# 제휴문의 페이지
def contact(request):
    return render(request, 'pages/contact.html')

# 채용 페이지
def recruit(request):
    return render(request, 'pages/recruit.html')