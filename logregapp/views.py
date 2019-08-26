from django.db import transaction
from django.shortcuts import render, HttpResponse, redirect
from logregapp.captcha.image import ImageCaptcha
from logregapp.models import User
import string, random, time
# Create your views here.


def login(request):
    name = request.COOKIES.get("name")
    pwd = request.COOKIES.get("password")
    result = User.objects.filter(name=name, password=pwd)
    if result:
        request.session['login'] = 'ok'
        return redirect('emsapp:employee')
    return render(request, 'login.html')


def loginlogic(request):
    name = request.POST.get('username')
    pwd = request.POST.get("userpwd")
    rem = request.POST.get('remember')
    result = User.objects.filter(name=name, password=pwd)
    if result:
        request.session['login'] = 'ok'
        res = redirect('emsapp:employee')
        if rem:
            res.set_cookie('name', name, max_age=7 * 24 * 3600)
            res.set_cookie('password', pwd, max_age=7 * 24 * 3600)
        return res
    return redirect('logregapp:login')


def regist(request):
    return render(request, 'regist.html')


def registlogic(request):
    try:
        with transaction.atomic():
            name = request.POST.get("username")
            pwd = request.POST.get("userpwd2")
            in_codes = request.POST.get('captcha')
            codes = request.session.get('codes')
            print(codes)
            if in_codes.lower() == codes.lower():
                pass
            else:
                raise
            u = User.objects.create(name=name, password=pwd, realname='ww')
            if u:
                return redirect('logregapp:login')
    except:
        return redirect('logregapp:regist')


def getcaptcha(request):
    image = ImageCaptcha()
    codes = random.sample(string.ascii_letters+string.digits, 5)
    codes = ''.join(codes)
    request.session['codes'] = codes
    data = image.generate(codes)
    # print(data)
    return HttpResponse(data, 'image/png')


def checkname(request):
    time.sleep(1)
    name = request.POST.get('username')
    r = User.objects.filter(name=name)
    if r:
        return HttpResponse('/static/img/error.jpg')
    else:
        return HttpResponse('/static/img/right.jpg')


def checkPassword(request):
    time.sleep(1)
    pwd1 = request.POST.get('pwd1')
    pwd2 = request.POST.get('pwd2')
    if pwd1 == pwd2:
        return HttpResponse('密码一致')
    else:
        return HttpResponse('两次密码不一致')


def checkcap(request):
    in_codes = request.POST.get('captcha')
    codes = request.session.get('codes')
    # print(codes)
    if in_codes.lower() == codes.lower():
        return HttpResponse('验证通过')
    else:
        return HttpResponse('验证码错误')
