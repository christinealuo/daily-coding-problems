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

# Before and after not in map
# Before in map and after not in map - check for sequence
# Before not in map and after in map - check for sequence
# Before and after in map - before and after is 0, before is 0 and after is not, after is 0 and before is not

def problem_514(numbers):
    buckets = [[]]
    nextBucket = 1
    numberToBucket = {} # { 100: 0, 4: 0, 200: 0, 1: 0, 3: 1, 2: 1}
    longestBucket = 0
    for number in numbers:
        before = number - 1
        after = number + 1
        if (not before in numberToBucket) and (not after in numberToBucket):
            numberToBucket[number] = 0
        elif before in numberToBucket and (not after in numberToBucket):
            bucket = numberToBucket[before]
            if bucket == 0:
                bucket = nextBucket
                nextBucket += 1
                buckets.append([before])
            numberToBucket[number] = bucket
            buckets[bucket].append(number)
            if len(buckets[bucket]) > len(buckets[longestBucket]):
                longestBucket = bucket
        elif after in numberToBucket and (not before in numberToBucket):
            bucket = numberToBucket[after]
            if bucket == 0:
                bucket = nextBucket
                nextBucket += 1
                buckets.append([after])
            numberToBucket[number] = bucket
            buckets[bucket].append(number)
            if len(buckets[bucket]) > len(buckets[longestBucket]):
                longestBucket = bucket
        elif before in numberToBucket and after in numberToBucket:
            beforeBucket = numberToBucket[before]
            afterBucket = numberToBucket[after]
            if beforeBucket == 0 and afterBucket == 0:
                bucket = nextBucket
                nextBucket += 1
                buckets.append([before, number, after])
                numberToBucket[before] = bucket
                numberToBucket[number] = bucket
                numberToBucket[after] = bucket
            elif beforeBucket == 0 and afterBucket != 0:
                bucket = afterBucket
                buckets[bucket].extend([before, number])
                numberToBucket[before] = bucket
                numberToBucket[number] = bucket
            elif beforeBucket != 0 and afterBucket == 0:
                bucket = beforeBucket
                buckets[bucket].extend([number, after])
                numberToBucket[number] = bucket
                numberToBucket[after] = bucket
            else: # Before and after assigned to different buckets
                bucket = afterBucket
                buckets[bucket].extend([number] + buckets[beforeBucket])
                # TODO: make sure that all the numbers in the before bucket are updated in the map but that will add some more complexity
                numberToBucket[number] = bucket
            if len(buckets[bucket]) > len(buckets[longestBucket]):
                    longestBucket = bucket
    print(buckets)
    print(numberToBucket)
    return len(buckets[longestBucket]) # 4

numbers = [100, 4, 200, 1, 3, 2]
print(problem_514(numbers))