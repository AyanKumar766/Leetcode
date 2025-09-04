class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> lastIndex(256, -1); // stores last seen index of each char
        int maxLen = 0, start = 0;      // sliding window start
        
        for (int i = 0; i < s.size(); i++) {
            if (lastIndex[s[i]] >= start) {
                // move start to one after the last duplicate
                start = lastIndex[s[i]] + 1;
            }
            lastIndex[s[i]] = i; // update last seen index
            maxLen = max(maxLen, i - start + 1);
        }
        
        return maxLen;
    }
};
