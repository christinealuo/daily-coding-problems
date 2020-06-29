# Each number will be associated with a bucket number
# Each number begins at bucket 0 which is the default
# For each number, check of that number - 1 or that number + 1 exists in set
# If you find such number, if that number is already associated with a bucket, insert the new number into that same bucket
# If such number is not already associated with a bucket, create a new bucket and add those two numbers into it

# [100, 4, 200, 1, 3, 2]
# Map: { 100: 0, 4: 1, 200: 0, 1: 1, 3: 1, 2: 1}
# Buckets: [[], [3, 4, 2, 1]]

# O(N) to traverse the input array
# O(1) to put number into map and get -1/+1
# O(1) to access correct bucket and append new number to that bucket

def problem_514(numbers):
    buckets = [[]]
    nextBucket = 1
    numberToBucket = {} # { 100: 0, 4: 0, 200: 0, 1: 0, 3: 1, 2: 1}
    longestBucket = 0
    for number in numbers: # 2
        before = number - 1 # 1
        after = number + 1 # 3
        if (not before in numberToBucket) and (not after in numberToBucket):
            # No before and after
            numberToBucket[number] = 0
        elif before in numberToBucket and (not after in numberToBucket):
            # Seen before and before
            bucket = numberToBucket[before]
            if bucket == 0:
                # Create new bucket for before-number sequence
                bucket = nextBucket
                nextBucket += 1
                buckets.append([before])
            numberToBucket[number] = bucket
            buckets[bucket].append(number)
            # Update longest bucket if necessary
            if len(buckets[bucket]) > len(buckets[longestBucket]):
                longestBucket = bucket
            # After checking before, check after again to update after
            if after in numberToBucket:
                buckets[bucket].append(after)
                # Update longest bucket if necessary
                if len(buckets[bucket]) > len(buckets[longestBucket]):
                    longestBucket = bucket
        elif after in numberToBucket: # 3
            bucket = numberToBucket[after] # 1
            if bucket == 0:
                # Create new bucket for number-after sequence
                bucket = nextBucket # 1
                nextBucket += 1 # 2
                buckets.append([after]) # [[], [4]]
            numberToBucket[number] = bucket
            buckets[bucket].append(number) # [[], [4, 3, 2]]
            # Update longest bucket if necessary
            if len(buckets[bucket]) > len(buckets[longestBucket]):
                longestBucket = bucket # 1
            # After checking after, check before again to update after
            if before in numberToBucket: # 1
                buckets[bucket].append(before) # [[], [4, 3, 2, 1]]
                # Update longest bucket if necessary
                if len(buckets[bucket]) > len(buckets[longestBucket]):
                    longestBucket = bucket
    print(buckets)
    print(numberToBucket)
    return len(buckets[longestBucket]) # 4

numbers = [100, 4, 200, 1, 3, 2]
print(problem_514(numbers))