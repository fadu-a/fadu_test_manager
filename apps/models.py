from django.db import models

class Test_error_logs(models.Model):
        test_cases = models.ForeignKey('Test_cases', on_delete=models.CASCADE)
        Data = models.TextField()

        def __str__(self):
                return self.Data

class Test_io_logs(models.Model):
        test_cases = models.ForeignKey('Test_cases', on_delete=models.CASCADE)
        Timestamp = models.DateTimeField()
        Percentile = models.FloatField()
        Wr_iops = models.FloatField()
        Wr_throughput = models.FloatField()
        Wr_latency = models.FloatField()
        Rd_iops = models.FloatField()
        Rd_throughput = models.FloatField()
        Rd_latency = models.FloatField()

class Test_smart_logs(models.Model):
        test_cases = models.ForeignKey('Test_cases',on_delete=models.CASCADE)
        Timestamp =  models.DateTimeField()
        Data_units_read = models.IntegerField()

class Test_cases(models.Model):
        pass

