import os

def read_data_file(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ranges = []
    with open(os.path.join(script_dir, filename), 'r') as f:
        # read the first line into a list of ranges
        line = f.readline().strip()
        range_strings = line.split(',')

        # get expanded form of each range
        for range_string in range_strings:
            start_str, end_str = range_string.split('-')
            start, end = int(start_str), int(end_str)
            expanded_range = []
            for num in range(start, end + 1):
                expanded_range.append(str(num))
            ranges.append(expanded_range)

    return ranges

def is_invalid_id(num):
    if len(num) % 2 != 0:
        return False
    
    # single sequence should take up half the string for invalid ids
    first_half = num[:len(num) // 2]
    second_half = num[len(num) // 2:]
    
    # check if this sequence is repeated twice
    return first_half == second_half

def find_invalid_ids(ranges):
    invalid_ids = []
    for range in ranges:
        for num in range:
            if is_invalid_id(num):
                invalid_ids.append(int(num))
    return invalid_ids

def day_2():
    ranges = read_data_file('day_2.txt')
    invalid_ids = find_invalid_ids(ranges)
    print(sum(invalid_ids))

if __name__ == '__main__':
    day_2()
