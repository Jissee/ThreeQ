
//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int C(int a, int b) {
    long int up = 1;
    long int down = 1;
    if (b == 0) {
        return 1;
    }
    while (b >= 1) {
        up *= a;
        down *= b;
        a -= 1;
        b -= 1;
}
        

    return up / down;
}

int main()
{
    int n = 0, A = 0, m = 0, sum0 = 0, sum1 = 0;
    int N0 = 0, N1 = 0, Y0 = 0, Y1 = 0;
    double prob = 0.0, probN0Y1 = 0.0, probN1Y0 = 0.0;
    double probsum = 0;
    char* str;
    str = (char*)malloc(10010);
    FILE* fstream;
    freopen_s(&fstream, "in.txt", "r", stdin);
    fill(str, str + 10010, '\0');
    cin >> n >> A >> m;
    cin >> str;
    prob = double(A) / 100;
    probN0Y1 = prob;
    probN1Y0 = 1 - prob;
    for (int i = 1; i <= n; i++) {
        if (str[i - 1] == '0') {
            sum0 += 1;
        }
        else {
            sum1 += 1;
        }
    }
    //sum0=2,sum1=1
//mm要中的个数，n总个数=sum0+sum1
    if (n <= 50) {
        for (int mm = m; mm <= n; mm++) {//n-5<=mm<=n
            if (sum0 > mm) {
                Y0 = mm;
            }
            else {
                Y0 = sum0;
            }
            Y1 = mm - Y0;
            N0 = sum0 - Y0;
            N1 = sum1 - Y1;
            while (Y1 <= sum1 and N0 >= 0){
                probsum += C(sum0,Y0) * C(sum1,Y1) * pow(probN0Y1,N0+Y1) * pow(probN1Y0,N1+Y0);
                N0 += 1;
                Y0 -= 1;
                N1 -= 1;
                Y1 += 1;
            }
        }
        cout << probsum;
    }else {
        cout << 1;
    }
    return 0;
}