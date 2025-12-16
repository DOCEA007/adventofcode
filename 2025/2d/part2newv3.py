with open('input.txt', 'r') as file:
    ranges = [i.split('-') for i in file.read().strip().split(',')]
    invalid=[]
    # print(ranges)
    with open('input.txt', 'r') as file:
        ranges = [part.split('-') for part in file.read().strip().split(',')]
        invalid_ids = []

        for id_range in ranges:
            start_id, end_id = map(int, id_range)
            min_digits = len(str(start_id))
            max_digits = len(str(end_id))

            for num_digits in range(min_digits, max_digits + 1):
                smallest_with_num_digits = 10 ** (num_digits - 1)
                largest_with_num_digits = 10 ** num_digits - 1

                if end_id < smallest_with_num_digits or start_id > largest_with_num_digits:
                    continue

                # repeat_count = how many times we repeat the pattern (at least 2)
                for repeat_count in range(2, num_digits + 1):
                    if num_digits % repeat_count != 0:
                        continue  # total length must be divisible by repeat_count

                    pattern_length = num_digits // repeat_count

                    # Pattern cannot start with zero, so pattern must be at least 10^(pattern_length-1)
                    pattern_min = 10 ** (pattern_length - 1)
                    pattern_max = 10 ** pattern_length - 1

                    for pattern_value in range(pattern_min, pattern_max + 1):
                        repeated_str = str(pattern_value) * repeat_count
                        candidate_id = int(repeated_str)

                        # Safety: ensure we really generated num_digits-digit numbers
                        if len(repeated_str) != num_digits:
                            continue

                        if candidate_id > end_id:
                            # Further pattern_value will only grow candidate_id, so break
                            break
                        if candidate_id < start_id:
                            continue

                        # Avoid counting duplicates (same number via different decompositions)
                        if candidate_id not in invalid_ids:
                            invalid_ids.append(candidate_id)
                            print(candidate_id)

        print(sum(invalid_ids))

                    
      


    print(sum(invalid))