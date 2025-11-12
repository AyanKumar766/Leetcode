#include <stdlib.h>

static int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int minOperations(int* nums, int numsSize) {
    int n = numsSize;
    int count1 = 0;
    for (int i = 0; i < n; ++i) {
        if (nums[i] == 1) {
            ++count1;
        }
    }
    if (count1 > 0) {
        return n - count1;
    }
    int minLen = n + 1;
    for (int i = 0; i < n; ++i) {
        int g = nums[i];
        for (int j = i + 1; j < n; ++j) {
            g = gcd(g, nums[j]);
            if (g == 1) {
                int len = j - i + 1;
                if (len < minLen) {
                    minLen = len;
                }
                break;
            }
        }
    }
    if (minLen == n + 1) {
        return -1;
    }
    return (minLen - 1) + (n - 1);
}
