class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        int sum=0;
        for(int i=0;i<nums.size();i++){
            sum=sum+nums[i];
        }
        int lsum=0;
        int rsum=sum;
        for(int i=0;i<nums.size();i++){
            rsum=rsum-nums[i];
            if(lsum==rsum){
                return i;
            }
            lsum=lsum+nums[i];
            
        }
        return -1;
    }
};