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
        self.diff = weight-length

    @classmethod
    def create_from_line(cls, line):
        weight, length = map(int, line.strip().split())
        return cls(weight, length)


class Diff(object):
    """ 每个diff一致的Jobs的集合,不能存在2个 diff 的 self.diff 一致 """
    def __init__(self, diff):
        self.diff = diff
        self.data = []  # 里面存的是每个 jobs 的 weight 的相反数

    def insert(self, job):
        heapq.heappush(self.data, -job.weight)


class Diff_heap(object):
    """ 所有的 diff 构成的集合 """

    def __init__(self):
        self.index = []
        self.index_dict = {}
        self.data = {}
        pass

    def insert(self, diff):
        heapq.heappush(self.index, diff.diff)
        self.data[diff.diff] = diff
        self.index_dict[diff.diff] = True


file_obj = open(file_path, 'r')
line_number = int(file_obj.readline().strip())
diff_heap = Diff_heap()

for i in range(line_number):
    job = Job.create_from_line(file_obj.readline())
    if job.diff not in diff_heap.index_dict:
        diff = Diff(job.diff)
        diff.insert(job)
        diff_heap.insert(diff)
    else:
        diff_heap.data[job.diff].insert(job)

