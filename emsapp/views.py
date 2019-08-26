from django.core.paginator import Paginator
from django.shortcuts import render, redirect ,HttpResponse
from django.urls import reverse

from emsapp.models import Employeelist
import uuid, os
# Create your views here.


def employee(request):
    pagtor = Paginator(Employeelist.objects.all(), per_page=3)
    # print(pagtor.count)
    # print(pagtor.page_range)
    # print(pagtor.num_pages)
    n = request.GET.get('number', 1)
    try:
        if int(n) not in pagtor.page_range:
            n = 1
    except:
        n = 1
    page = pagtor.page(n)
    status = request.session.get('login')
    if status:
        return render(request, "emplist.html", {
            'ems': page
        })
    return redirect('logregapp:login')


def upload(request):
    headpic = request.FILES.get('headpic')
    ext = os.path.splitext(headpic.name)
    headpic.name = str(uuid.uuid4())+ext[1]
    name = request.POST.get('name')
    salary = request.POST.get('salary')
    age = request.POST.get('age')
    pagtor = Paginator(Employeelist.objects.all(), per_page=3)
    pages = pagtor.num_pages
    # print(pages)
    page = pagtor.page(pages)
    # print(len(page.object_list))
    if len(page.object_list) == 3:
        pages += 1
    # print(pages)
    Employeelist.objects.create(headpic=headpic, name=name, salary=salary, age=age)
    return redirect(reverse('emsapp:employee')+'?number=%s' % pages)


def add(request):
    return render(request, 'addEmp.html')


def update(request):
    pa_num = request.GET.get('number')
    print(pa_num)
    id = request.GET.get('id')
    em = Employeelist.objects.get(id=id)
    request.session['id'] = id
    request.session['pa_num'] = pa_num
    return render(request, 'updateEmp.html', {
        'em': em
    })


def updatelogic(request):
    id = request.session.get('id')
    em = Employeelist.objects.get(id=id)
    name = request.POST.get('name')
    headpic = request.FILES.get('headpic')
    # print(file)
    ext = os.path.splitext(headpic.name)
    headpic.name = str(uuid.uuid4()) + ext[1]
    salary = request.POST.get('salary')
    age = request.POST.get('age')
    em.name = name
    em.headpic = headpic
    em.salary = salary
    em.age = age
    em.save()
    page = request.session.get('pa_num')
    print(page)
    return redirect(reverse('emsapp:employee')+'?number=%s' % page)


def delete(request):
    id = request.GET.get('id')
    pagtor = Paginator(Employeelist.objects.all(), per_page=3)
    pages = request.GET.get('number')
    print(pages)
    page = pagtor.page(pages)
    # print(len(page.object_list))
    if len(page.object_list) == 1:
        pages -= 1
    em = Employeelist.objects.get(id=id)
    em.delete()
    return redirect(reverse('emsapp:employee')+'?number=%s' % pages)


