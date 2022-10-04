class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n=nums.size();
        vector<int> temp(2*nums.size());
        for(int i=0;i<nums.size();i++){
            temp[i]=nums[i];
            temp[i+n]=nums[i];
            
        }
        return temp;
    }
};