from ctypes import *
lib = CDLL("./Dll1.dll")
from tqdm import *

arr = [1, 2, 3, 4, 5]
arr_c = (c_int * len(arr))(*arr) # по сути мы должны сначала создать
# массив на понятном для плюсов языке а уже потом закидывать его в нашу функцию


for i in tqdm(range(10000)):
    result = lib.sum_array(arr_c, len(arr))
    print(result)