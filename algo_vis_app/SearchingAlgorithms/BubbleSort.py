def bubble_sort(nums):
    algorithm_info = {
        'comparisons': [],
        'swaps': [] #indices
    }

    last_sorted_elem = len(nums)
    for i in range(last_sorted_elem-1):

        for j in range(0, last_sorted_elem-i-1):

            if nums[j] > nums[j+1]:
                algorithm_info['comparisons'].append((j,j+1))
                nums[j], nums[j+1] = nums[j+1], nums[j] #swapping
                algorithm_info['swaps'].append((j+1,j))
            else:
                algorithm_info['comparisons'].append((j,j+1))
                algorithm_info['swaps'].append((None))


    return algorithm_info

