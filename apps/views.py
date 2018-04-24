from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TestIoLogs, TestCases
from django.shortcuts import render
import json


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
