from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class TestErrorLogs(models.Model):
        test_cases = models.ForeignKey('TestCases', on_delete=models.CASCADE)
        Data = models.TextField()

        def __str__(self):
                return self.Data


class TestIoLogs(models.Model):
        test_cases = models.ForeignKey('TestCases', on_delete=models.CASCADE)
        Timestamp = models.DateTimeField()
        Percentile = models.FloatField()
        Wr_iops = models.FloatField()
        Wr_throughput = models.FloatField()
        Wr_latency = models.FloatField()
        Rd_iops = models.FloatField()
        Rd_throughput = models.FloatField()
        Rd_latency = models.FloatField()


class TestSmartLogs(models.Model):
        test_cases = models.ForeignKey('TestCases', on_delete=models.CASCADE)
        Timestamp = models.DateTimeField()
        Data_units_read = models.IntegerField()


class TestLogs(models.Model):
        id = models.IntegerField(primary_key=True)
        user_id = models.IntegerField()
        test_suit_id = models.IntegerField()
        test_date = models.DateTimeField(default=timezone.now)
        status = models.CharField(max_length=100)


class TestSuits(models.Model):
        id = models.IntegerField(primary_key=True)


class Users(models.Model):
        id = models.IntegerField(primary_key=True)


class TestCases(models.Model):
        test_group_id = models.IntegerField(default=1)
        title = models.CharField(max_length=100, null=True)
        description = models.CharField(null=True, max_length=100)
        configs = JSONField(null=True, blank=True)
