def sum_of_intervals(intervals):

    intervals.sort(reverse=False, key=lambda e: e[0])

    intervals = [list(e) for e in intervals]

    for i in range(len(intervals) - 1):
        if (intervals[i][1] > intervals[i+1][0] and intervals[i][1] <= intervals[i+1][1]):
            intervals[i+1][0] = intervals[i][0]

            intervals[i][0] = 0
            intervals[i][1] = 0
        elif (intervals[i][1] > intervals[i+1][0] and intervals[i][1] > intervals[i+1][1]):
            intervals[i+1][0] = intervals[i][0]
            intervals[i+1][1] = intervals[i][1]

            intervals[i][0] = 0
            intervals[i][1] = 0

    intervals = [e[1]-e[0] for e in intervals]

    return sum(intervals)


print(sum_of_intervals([(-305, 390), (119, 293), (30, 62), (163, 395), (-359, 23)]))
