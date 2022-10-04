class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> temp(nums.size());
        for(int i=0;i<nums.size();i++){
            temp[i]=nums[nums[i]];
            
        }
        return temp;
    }
};