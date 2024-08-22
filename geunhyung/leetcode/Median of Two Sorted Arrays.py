# 링크: https://leetcode.com/problems/median-of-two-sorted-arrays/
# 시간: 87ms
# 메모리: 16.78MB

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        l = len(nums1) + len(nums2)
        list_sorted = sorted(nums1 + nums2)
        return (list_sorted[l//2] + list_sorted[l//2-1]) / 2 if l % 2 == 0 else list_sorted[l//2]