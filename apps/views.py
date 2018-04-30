from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TestIoLogs, TestCases
from django.shortcuts import render, redirect
import urllib.request
import json
from urllib.error import HTTPError, URLError
from .forms import NewForm
from collections import OrderedDict
import requests


@csrf_exempt
def post_results(request, pk):
    data = json.loads(request.body)
    data["test_cases_id"] = pk
    test = TestIoLogs.objects.create(**data)
    test.save()
    return HttpResponse(request.POST)


def result_list(request):
    servers = list(TestCases.objects.values('Title', 'id'))
    print(servers)
    servers2 = {}
    servers2['datas'] = servers

    return render(request, 'results/result_form.html', servers2)


def view_detail(request, pk):
    data = TestIoLogs.objects.filter(test_cases_id=pk)
    data2 = {}
    data2['datas'] = data
    print(data2)
    return render(request, 'results/result_detail.html', data2)


def runner_check(request):
    URLs = ['http://localhost:3000', 'http://localhost:8000', 'http://localhost:5000']
    runners_data = []

    for url in URLs:
        ip = url.split('//')[1].split(':')[0]
        port = url.split(':')[2]
        req = urllib.request.Request(url + '/status')
        try:
            response = urllib.request.urlopen(req)
            data = response.read()
            encoding = response.info().get_content_charset('utf-8')
            info = json.loads(data.decode(encoding))
            status = "Successful"
        except HTTPError as e:
            status = "Failed"
            info = ""
        except URLError as e:
            status = "Failed"
            info = ""
        runners_data.append({'ip': ip, 'port': port, 'status': status, 'info': info})
    return render(request, 'apps/status.html', {'runners_data': runners_data})


def get_index(request):
    list = TestCases.objects.all().order_by('-pk')
    return render(request, 'apps/index.html', {'list': list})


def detail(request, id):
    data = TestCases.objects.filter(id=id)
    return render(request, 'apps/detail.html', {'data_list': data})


def post_new(request):
    if request.method == "POST":
        request.POST._mutable = True
        post_value = request.POST
        post_value.update(Configs=json.dumps(post_value['Configs']))
        form = NewForm(post_value)
        if form.is_valid():
            post = form.save(commit=False)
            post.Test_group_id = 1
            post.save()
            return redirect('testcase:index')
    else:
        form = NewForm()
        return render(request, 'apps/new.html', {'form': form})


def post_edit(request, id):
    if request.method == "POST":
        request.POST._mutable = True
        post_value = request.POST
        post_value.update(Configs=json.dumps(post_value['Configs']))
        form = NewForm(post_value)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = id
            post.Test_group_id = 3
            post.save()
            return redirect('testcase:index')
    else:
        row = TestCases.objects.get(id=id)
        form = NewForm(initial={'Title': row.Title, 'Description': row.Description, 'Configs': row.Configs})
        return render(request, 'apps/edit.html', {'form': form})


def delete(id):
    delete_value = TestCases.objects.get(id=id)
    delete_value.delete()
    return redirect('testcase:index')


def run_test(request, id):
    data = TestCases.objects.get(id=id)
    configs = data.Configs.split(', ')
    dic_configs = OrderedDict()
    for list in configs:
        list = list.split(':')
        dic_configs[list[0]] = list[1]
    json_data = json.dumps(dic_configs)
    url = 'http://localhost:5000/start'
    headers = {'content-type': 'application/json'}
    res = requests.post(url, data=json_data, headers=headers)
    return render(request, 'results/result_form.html', {'res': res})
