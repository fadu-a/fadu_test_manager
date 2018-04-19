from django.shortcuts import render
import urllib.request
import json


def testRunner_check(request):
        webURL = urllib.request.urlopen('http://localhost:8000/runners/status')
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        json_data = json.loads(data.decode(encoding))
        return render(request, 'apps/status.html', {'data': json_data})
