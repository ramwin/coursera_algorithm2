#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-09-11 22:52:12

file_path = "data/jobs.txt"


import heapq

class Job(object):
    """ Job """
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.ratio_minus = -weight/length

    @classmethod
    def create_from_line(cls, line):
        weight, length = map(int, line.strip().split())
        return cls(weight, length)


class Job_heap(object):
    """ 所有的 diff 构成的集合 """

    def __init__(self):
        self.index = []  # [-1.1, -1.34, -1.43] 所有-weight/length的集合
        self.data = {}  # {-0.5: [job1, job2]}
        pass

    def insert(self, job):
        if job.ratio_minus in self.data:
            self.data[job.ratio_minus].append(job)
        else:
            heapq.heappush(self.index, job.ratio_minus)
            self.data[job.ratio_minus] = [job,]


file_obj = open(file_path, 'r')
line_number = int(file_obj.readline().strip())
job_heap = Job_heap()

for i in range(line_number):
    job = Job.create_from_line(file_obj.readline())
    job_heap.insert(job)

duration = 0  # 随着job的完成，这个duration会一直增加
cost = 0
while job_heap.index:
    ratio_minus = heapq.heappop(job_heap.index)
    for job in job_heap.data[ratio_minus]:
        duration += job.length
        cost += job.weight*duration
print(cost)
