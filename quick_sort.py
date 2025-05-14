class Solution:
    def fun(self, num, l, h):
        piv = num[l]
        i = low + 1
        j = high
        while i < j:
            while i <= high and num[i] <= piv:
                i += 1
            while j >= low and num[j] > piv:
                j -= 1
            if i >= j: #-- if i < j : swap(num[i], num[j])
                break
            num[i], num[j] = num[j], num[i]
        num[l], num[j] = num[j], num[l]
        return j

    def sorting(self, num, l, h):
        if l < h:
            p = self.fun(num, l, h)
            self.sorting(num, l, p - 1)
            self.sorting(num, p + 1, h)

    def quickSort(self, nums):
        self.sorting(nums, 0, len(nums) - 1)
        return nums


# input_str.strip() → Removes any leading/trailing whitespace.

# .split() → Splits the string into a list of substrings using spaces: ['4', '7', '2', '1']

# map(int, ...) → Converts each string to an int.

# list(...) → Wraps the map object into a list: [4, 7, 2, 1]


if __name__ == "__main__"
input_str = input("Enter numbers seperated ny spaces")
arr = list(map(int, input_str.strip().spilt()))

sorter = Solution()

print("original array: ", arr)
answer = sorter.quickSort(arr)
print("Sorted array: ", arr)

