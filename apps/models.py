from django.db import models
from django.contrib.postgres.fields import JSONField


class TestSuits(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    io_tester = models.CharField(max_length=10)


class TestGroups(models.Model):
    id = models.AutoField(primary_key=True)
    Test_suits_id = models.ForeignKey(TestSuits, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Dependency_id = models.IntegerField()
    Configs = JSONField()


class TestCases(models.Model):
    id = models.AutoField(primary_key=True)
    Test_group_id = models.ForeignKey(TestGroups, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Configs = JSONField()


class TestErrorLogs(models.Model):
    test_cases = models.ForeignKey('TestCases', on_delete=models.CASCADE)
    Data = models.TextField()


class TestIoLogs(models.Model):
    test_cases = models.ForeignKey('TestCases', on_delete=models.CASCADE)
    Timestamp = models.IntegerField()
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
