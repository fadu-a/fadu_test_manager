from apps.models import TestErrorLogs, TestIoLogs, TestSmartLogs, TestCases
from django.contrib import admin

admin.site.register(TestIoLogs)
admin.site.register(TestSmartLogs)
admin.site.register(TestCases)
admin.site.register(TestErrorLogs)