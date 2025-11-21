#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> A;
    set<int> B;
    int n = 0;
    int element = 0;

    cout << "Enter amount of elements for A: " << endl;
    cin >> n;
    cout << "Enter the elements for set A: " << endl;
    for (int i = 0; i < n; i++) {
        cin >> element;
        A.insert(element);
    }

    cout << "Enter amount of elements for B: " << endl;
    cin >> n;
    cout << "Enter the elements for set B: " << endl;
    for (int i = 0; i < n; i++) {
        cin >> element;
        B.insert(element);
    }
    int countA = A.size();
    int countB = B.size();

    if (countA < countB) {
        for (int elA : A) { // берём все элементы A
            cout << elA << endl;
        }
        cout << endl;
    }
    else if (countB < countA) {
        for (int elB : B) { // берём все элементы B
            cout << elB << endl;
        }
    }
    else {
        cout << "Sets have the same amount of elements" << endl;
    }
    system("pause");
    return 0;
}