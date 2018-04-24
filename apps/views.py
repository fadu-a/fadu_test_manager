from django.shortcuts import render, redirect
from .forms import NewForm
import urllib.request
import json
from urllib.error import HTTPError, URLError


def runner_check(request):
    URLs = ['http://localhost:8000', 'http://localhost:9000']
    runners_data = []

    for url in URLs:
        ip = url.split('//')[1].split(':')[0]
        port = url.split(':')[2]
        req = urllib.request.Request(url + '/runners/status')
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


def post_new(request):
    if request.method == "POST":
        request.POST._mutable = True
        post_value = request.POST
        post_value.update(configs=json.dumps(post_value['configs']))
        form = NewForm(post_value)
        if form.is_valid():
            post = form.save(commit=False)
            post.test_group_id = 1
            post.save()
            return redirect('testcase_new')
    else:
        form = NewForm()
        return render(request, 'apps/new.html', {'form': form})
