/*
 * @lc app=leetcode id=121 lang=cpp
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice=prices[0];
        int profit=0;
        for(int i=1;i<prices.size();i++){
            minPrice=min(minPrice, prices[i]);
            profit=max(profit, prices[i]-minPrice);
            }

            return profit;
    }
};
// @lc code=end

