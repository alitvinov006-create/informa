#include <iostream>
using namespace std;

int main() {
    const int k = 5;
  
    int A[k];
    int B[k];

    cout << "Enter elements for array A: " << endl;
    for (int i = 0; i < k; i++) {
        cin >> A[i];
    }

    cout << "Enter elements for array B: " << endl;;
    for (int i = 0; i < k; i++) {
        cin >> B[i];
    }

    int countA = 0;
    int countB = 0;

    for (int i = 0; i < k; i++) {
        if (A[i] % 2 == 0) {
            countA += 1;
        }
        if (B[i] % 2 == 0) {
            countB += 1;
        }
    }
    if (countA >= countB) {
        for (int i = 0; i < k; i++) {
            cout << A[i] << endl;
        }
    }
    else {
        for (int i = 0; i < k; i++) {
            cout << B[i] << endl;
        }
    }

    return 0;
    system("pause");
}