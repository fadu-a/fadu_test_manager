from django.contrib import admin
from apps.models import Test_error_logs, Test_io_logs, Test_smart_logs, Test_cases

admin.site.register(Test_io_logs)
admin.site.register(Test_smart_logs)
admin.site.register(Test_cases)
admin.site.register(Test_error_logs)
