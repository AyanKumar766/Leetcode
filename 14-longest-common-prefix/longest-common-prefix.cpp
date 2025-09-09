class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";

        // Sort strings
        sort(strs.begin(), strs.end());

        // Compare only the first and last string
        string first = strs.front();
        string last = strs.back();
        int i = 0;

        while (i < first.size() && i < last.size() && first[i] == last[i]) {
            i++;
        }

        return first.substr(0, i);
    }
};
