#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;

int main() {
	float x = 0;
	float y = 0;
	cin >> x;
	cin >> y;
	float r = 2 * sin((x + y) / 2) * cos((x - y) / 2);
	float s = pow(exp(1), 2) * log(x);
	cout << r << endl;
	cout << s << endl;
	float c = max(r, s);
	cout << c << endl;
	system("pause");
	return 0;
}