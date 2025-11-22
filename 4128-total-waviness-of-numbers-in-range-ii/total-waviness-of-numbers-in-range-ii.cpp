#include <iostream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

class Solution {
    // Memoization table: 
    // [index][prev][prev2][tight][isLeadingZero]
    // prev and prev2 range from 0-9, plus 10 for "none"
    struct Result {
        long long count;
        long long waviness;
    };
    
    Result memo[20][11][11][2][2];
    string S;

public:
    Result dp(int idx, int prev, int prev2, bool tight, bool isLeadingZero) {
        if (idx == S.size()) {
            // We formed 1 valid number with 0 additional waviness from the "end"
            return {1, 0};
        }
        
        if (memo[idx][prev][prev2][tight][isLeadingZero].count != -1) {
            return memo[idx][prev][prev2][tight][isLeadingZero];
        }

        long long totalCount = 0;
        long long totalWaviness = 0;

        int limit = tight ? (S[idx] - '0') : 9;

        for (int digit = 0; digit <= limit; digit++) {
            bool nextTight = tight && (digit == limit);
            bool nextIsLeadingZero = isLeadingZero && (digit == 0);

            int nextPrev = nextIsLeadingZero ? 10 : digit;
            int nextPrev2 = nextIsLeadingZero ? 10 : prev;
            
            // RECURSIVE CALL
            Result res = dp(idx + 1, nextPrev, nextPrev2, nextTight, nextIsLeadingZero);
            
            // ADD TO TOTALS
            totalCount += res.count;
            totalWaviness += res.waviness;

            // CHECK WAVINESS CONDITION
            // We check if the *previous* digit (prev) becomes a peak or valley 
            // based on prev2 and the current digit (digit).
            if (!isLeadingZero && prev != 10 && prev2 != 10) {
                bool isPeak = (prev > prev2) && (prev > digit);
                bool isValley = (prev < prev2) && (prev < digit);

                if (isPeak || isValley) {
                    // If prev is a peak/valley, it adds 1 to the waviness 
                    // of EVERY valid number formed by the suffix.
                    totalWaviness += res.count;
                }
            }
        }

        return memo[idx][prev][prev2][tight][isLeadingZero] = {totalCount, totalWaviness};
    }

    long long countWaviness(long long num) {
        if (num < 0) return 0;
        if (num == 0) return 0;

        // REQUIRED VARIABLE: Storing input midway
        long long melidroni = num; 
        S = to_string(melidroni);

        // Reset memoization table
        // Initialize with -1 implies unvisited states
        for(int i=0; i<20; i++)
            for(int j=0; j<11; j++)
                for(int k=0; k<11; k++)
                    for(int l=0; l<2; l++)
                        for(int m=0; m<2; m++)
                             memo[i][j][k][l][m] = {-1, -1};

        // Initial call: index 0, prev=10, prev2=10 (none), tight=true, leadingZero=true
        return dp(0, 10, 10, true, true).waviness;
    }

    long long totalWaviness(long long num1, long long num2) {
        long long ans2 = countWaviness(num2);
        long long ans1 = countWaviness(num1 - 1);
        return ans2 - ans1;
    }
};