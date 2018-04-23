from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import TestIoLogs, TestCases
from django.shortcuts import render, redirect
import json
from .forms import PostForm

@csrf_exempt
def index(request):
    #test1 = json.loads(request.body.decode('utf-8'))
    #print(request.POST.id)
    myDict = dict(request.POST.lists())
    print(myDict)
    #case = TestCases.objects.get(id=1)
    #case = PostForm(request.POST)
    case = TestCases()


    print(case)
    case.save()
    test = TestIoLogs(test_cases_id=case.id,
                      Timestamp=timezone.now(),
                      Percentile=3.5,
                      Wr_iops=4,
                      Wr_latency=134,
                      Wr_throughput=444.4,
                      Rd_iops=1,
                      Rd_latency=21,
                      Rd_throughput=9.9)
    test.save()
    return HttpResponse(request.POST)


def result_list(request):
    servers = list(TestCases.objects.values('Title', 'id'))
    # print(servers)

    servers2 = {}
    servers2['datas'] = servers
#    print(servers2)

    return render(request, 'results/result_form.html', servers2)


def view_detail(request, pk):
    data = TestIoLogs.objects.filter(test_cases_id=pk)
    #list(TestIoLogs.objects.values(pk))
 #   print(data.Timestamp)
    data2 = {}
    data2['datas'] = data
    print(data2)
    return render(request, 'results/result_detail.html', data2)
