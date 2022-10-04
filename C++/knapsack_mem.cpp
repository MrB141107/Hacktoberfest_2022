//Knapsack using memoisation

#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> t(102, vector<int> (1002, -1)); 

int solve(vector<int> wt, vector<int> val, int w, int n){
	if(n==0 || w==0){
		return 0;
	}
	if(t[n][w]!=-1){
		return t[n][w];
	}
	if(wt[n-1]<=w){
		return t[n][w] = max( val[n-1]+solve(wt, val, w-wt[n-1], n-1), solve(wt, val, w, n-1));
	}
	else{
		return t[n][w] = solve(wt, val, w, n-1);
	}
}
	
int main(){
	int n = 4;
	int w = 7;	
	vector<int> wt = {1, 3, 4, 5};
	vector<int> val = {1, 4, 5, 7};
	
	cout<<solve(wt, val, w, n)<<"\n";
	return 0;
}