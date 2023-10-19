# 程式中的註解：寫給人看得，用來做紀錄、說明
# 第一支程式
# 撰寫程式、檔案、附檔名用 py
# 執行程式：python 檔案名稱

import winsound
from time import sleep

#print("hello python")

#beep alert
'''
for i in range(6,-1,-1):
    freq = 500*((1.03)**i)
    print(int(freq), end = " ")
print("")
for i in range(0,7):
    freq = 500*((1.122)**i)
    #winsound.Beep(int(freq), 500)
'''

#shining light
'''
#warrning_msg = "angel liao is cute"
warrning_msg = " url is dot!"
print(len(warrning_msg), end = "")
for i in range(10):   
    sleep(0.5)
    print(warrning_msg, end = "", flush=True)
    sleep(0.5)
    print(len(warrning_msg)*"\b"+len(warrning_msg)*" ", end ='', flush = True)
    print(len(warrning_msg)*"\b", end ='', flush = True)
'''
import sys
import os
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
if len(sys.argv) == 2:
    a = sys.argv[1]
else:
    a = 0
print(a)
#print(sys.argv[1])
a = input()
os.system('start.py ' + str(a))

#5 25 39