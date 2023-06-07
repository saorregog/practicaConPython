def pick_peaks(arr):
    result = {
        "pos": [],
        "peaks": []
    }

    if (len(arr) == 0):
        return result

    start_index = int()
    end_index = int()

    for i in range(len(arr) - 1):
        if (arr[i] != arr[i+1]):
            start_index = i + 1
            break

    for j in range(len(arr) - 1, 0, -1):
        if (arr[j] != arr[j-1]):
            end_index = j - 1
            break

    for i in range(start_index, end_index + 1):
        if (arr[i] > arr[i-1] and arr[i] >= arr[i+1]):

            for j in range(i, end_index + 1):
                if (arr[j] > arr[j+1]):
                    result["pos"].append(i)
                    result["peaks"].append(arr[i])
                    break
                elif (arr[j] < arr[j+1]):
                    break           

    return result


print(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]))