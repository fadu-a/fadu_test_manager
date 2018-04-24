from django.contrib import admin
from apps.models import TestErrorLogs, TestIoLogs, TestSmartLogs, TestCases

admin.site.register(TestIoLogs)
admin.site.register(TestSmartLogs)
admin.site.register(TestCases)
admin.site.register(TestErrorLogs)
