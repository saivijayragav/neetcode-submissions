"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        events.sort()
        ret = 0
        cur = 0
        for inter, diff in events:
            cur += diff
            ret = max(ret, cur)
        return ret
