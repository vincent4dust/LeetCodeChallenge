"""
Given non-overlapping intervals, intervals where intervals[i] = [start(i), end(i)] represent the start and the end of the ith interval
and intervals is sorted in ascending order by start(i).
Given newInterval = [start, end], insert newInterval into intervals such that intervals is still sorted in ascending order by start(i), and intervals still does not have
any overlapping intervals
return intervals after the insertion
"""

def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        result.append(newInterval)
        return result