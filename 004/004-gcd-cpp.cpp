#include<iostream>
#include<algorithm>
using namespace std;   

//We know that we can find the GCD of two numbers using Euclidean Algorithm like this:

//int gcd(int a, int b){
    //if(b==0)
        //return a;
    //else
        //return gcd(b,a%b);
//}

//But do you know that there is a built in function called __gcd() to find the GCD in the algorithm header file?

int main(){
    cout<<__gcd(18,27)<<endl;
    return 0;
}
