#pragma once

#ifdef MYLIBRARY_EXPORTS
#define MYLIBRARY_API __declspec(dllexport)
#else
#define MYLIBRARY_API __declspec(dllimport)
#endif

extern "C" {
    __declspec(dllexport) MYLIBRARY_API int sum_array(int* arr, int size);
}