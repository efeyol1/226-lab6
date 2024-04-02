#include <iostream>
#include <cmath>


using namespace std;

double func(int);
double func();
int main()
{
    cout << "Hello world!" << endl;
    cout <<  func(3) << endl;
    cout << func();

    return 0;
}
double func(int n){
    double sum=0.0;
    if(n>0){
    sum +=func(n-1) + pow(-1,n+1)/n;
    return sum;
    }

}
double func(){
    int n;
    cout << "enter n:";
    cin >> n;
    double sum=0.0;
    if(n>0){
    sum +=func(n-1) + pow(-1,n+1)/n;
    return sum;
}
}
