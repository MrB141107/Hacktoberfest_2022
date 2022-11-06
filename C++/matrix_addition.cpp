#include<iostream>
using namespace std;

int main(){
    int x[3][3],y[3][3],c[0][0];
    cout << "Matrix 1" << endl;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cout << "Enter Value At "<< i+1 << ", " << j+1 <<": "<< endl;
            cin >> x[i][j];
        }
    }
    cout << "Matrix 2" << endl;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cout << "Enter Value At "<< i+1 << ", " << j+1 <<": "<< endl;
            cin >> y[i][j]; 
        }
    }
    cout << "Adding the two matrices:" << endl;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            c[i][j] = x[i][j] + y[i][j];
        }
    }
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cout << c[i][j] << " " << flush;
        }
        cout << endl;
    }
}

