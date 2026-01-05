#include "pch.h"
#include "Header.h"

#define MYLIBRARY_EXPORTS
using namespace std;


int summa = 0;


extern "C" {
	MYLIBRARY_API int sum_array(int* arr, int size) {
		int total = 0;
		for (int i = 0; i < size; i++) {
			total += arr[i];
		}
		return total;
	}
}