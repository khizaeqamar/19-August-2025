# Array Problems

# Find two numbers in array that add up to the target.
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Delete extra duplicates and keep only unique numbers.
def remove_duplicates(nums):
    return list(set(nums))


# Join two sorted arrays into one sorted array.
def merge_sorted(nums1, nums2):
    return sorted(nums1 + nums2)


# Push all 0’s to the end, keep other numbers in order.
def move_zeroes(nums):
    return [x for x in nums if x != 0] + [0] * nums.count(0)


# Check if any number appears more than once return true else false.
def contains_duplicate(nums):
    return len(nums) != len(set(nums))


# Find the number that appears only once while others appear twice.
def single_number(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num
    return None


# Find the number that appears more than n/2 times.
def majority_element(nums):
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num
    return None


# Find the missing number from 0 to n.
def missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)


# Find numbers missing from 1 to n.
def find_disappeared_numbers(nums):
    n = len(nums)
    return [i for i in range(1, n+1) if i not in nums]


# Find common numbers between two arrays.
def find_common(nums1, nums2):
    return list(set(nums1) & set(nums2))



# Check if two strings have the same letters.
def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Check if a string reads the same forward and backward.
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


# Reverse the characters of a string.
def reverse_string(s):
    return s[::-1]
