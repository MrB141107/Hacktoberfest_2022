//Knapsack top-down

#include <bits/stdc++.h>
using namespace std;

int solve(vector<int> wt, vector<int> val, int w, int n, vector<vector<int>>& t){
	for(int i=1; i<n+1; i++){
		for(int j=1; j<w+1; j++){
			if(wt[i-1]<=j){
				t[i][j] = max(val[i-1]+ t[i-1][j-wt[i-1]], t[i-1][j]);
			}
			else{
				t[i][j] = t[i-1][j];
			}
		}
	}
	return t[n][w];
}

int main(){
	int n = 4, w = 7;
	vector<int> wt = {1, 3, 4, 5};
	vector<int> val = {1, 4, 5, 7};
	vector<vector<int>> t(n+1, vector<int> (w+1, 0));
	cout<<solve(wt, val, w, n, t)<<"\n";
	return 0;
}