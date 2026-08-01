"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        days = 0
        intervals.sort(key = lambda x: x.start)
        visited = set()
        for i, interval in enumerate(intervals):
            if i in visited:
                continue
            s, e = interval.start, interval.end
            days += 1
            visited.add(i)
            for j in range(i+1, len(intervals)):
                if j in visited:
                    continue
                if intervals[j].start >= e:
                    e = intervals[j].end
                    visited.add(j)
        return days