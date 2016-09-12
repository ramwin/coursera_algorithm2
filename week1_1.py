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
        self.sort = length-weight

    @classmethod
    def create_from_line(cls, line):
        weight, length = map(int, line.strip().split())
        return cls(weight, length)


class Diff(object):
    """ 每个diff一致的Jobs的集合,不能存在2个 diff 的 self.diff 一致 """
    def __init__(self, sort):
        self.sort = sort
        self.index = []  # 所有的-weight的排序
        self.data = {}  # 

    def insert(self, job):
        if -job.weight not in self.data:
            self.data[-job.weight] = []
            heapq.heappush(self.index, -job.weight)
        self.data[-job.weight].append(job)


class Diff_heap(object):
    """ 所有的 diff 构成的集合 """

    def __init__(self):
        self.index = []  # [0,1,2,3,4,5] 所有job.sort的集合
        self.data = {}  # diff 以 diff.diff 为Key, self为value的dict

    def insert(self, diff):
        heapq.heappush(self.index, diff.sort)
        self.data[diff.sort] = diff


file_obj = open(file_path, 'r')
line_number = int(file_obj.readline().strip())
diff_heap = Diff_heap()

for i in range(line_number):
    job = Job.create_from_line(file_obj.readline())
    if job.sort not in diff_heap.data:
        diff = Diff(job.sort)
        diff.insert(job)
        diff_heap.insert(diff)
    else:
        diff_heap.data[job.sort].insert(job)

duration = 0  # 随着job的完成，这个duration会一直增加
cost = 0
while diff_heap.index:
    sort = heapq.heappop(diff_heap.index)
    diff = diff_heap.data[sort]
    while diff.index:
        weight = -heapq.heappop(diff.index)
        for job in diff.data[-weight]:
            duration += job.length
            cost += duration* job.weight
print(cost)
