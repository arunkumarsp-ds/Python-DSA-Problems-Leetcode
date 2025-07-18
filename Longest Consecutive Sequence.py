def longestConsecutive(nums):
    set1 =  set(nums)
    max_sequence_length = 0

    for num in set1:
        if (num-1) not in set1:
            current_num = num
            current_sequence_length = 1
        
            while (current_num + 1) in set1:
                current_sequence_length += 1
                current_num += 1
            max_sequence_length = max(max_sequence_length,current_sequence_length)

    return max_sequence_length
