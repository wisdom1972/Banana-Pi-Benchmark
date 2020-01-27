# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:56:17 2020

D:\Tools\Python_tools\Python_examples\BPI_M64\bananapi_benchmark_2.py
Jan-27-2020: add the number product benchmark

@author: coworker
"""

# The benchmark test is by Wisdom Zhang, Jan-25-2020, 
# bananapi_benchmark.py
# the program is subject to test the BPI processor speed , based on Python. 
# it is based on Banana Pi M64
#
# i=1000000, the run time is  0:00:01.475983
# i=2000000, the run time is  0:00:02.777661
# i=4000000, the run time is  0:00:05.790657
# i=8000000, the run time is  0:00:12.492575
#
# it is based on Raspberry Pi 4
#
# i=1000000, the run time is  0:00:00.341868
# i=2000000, the run time is  0:00:00.677496
# i=4000000, the run time is  0:00:01.329719
# i=8000000, the run time is  0:00:02.837145
# i=32000000, the run time is  0:00:10.392236

# 2nd question,  sensehat expander board can not use in BPI, 
# 3rd question, I can not run the sudo rasp-config, I am not sure if the BPI SPI interface can not work, so, it lead to SenseHat board issue

# it is based on Lenovo E480 Notebook, Intel i5
#
# i=1000000, the run time is  0:00:00.111702
# i=2000000, the run time is  0:00:00.255029
# i=4000000, the run time is  0:00:00.493969
# i=8000000, the run time is  0:00:01.018509
# i=32000000, the run time is  0:00:03.999741




import datetime
import time

def calcProd(numberint):
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, numberint):
        product = product * i
    return product

startTime = time.time()
number1=100000
prod = calcProd(number1)
endTime = time.time()
print('The number product result is %s digits long.'% (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))


starttime1 = datetime.datetime.now()


# the all test benchmark, you need change only variable, from 1000000~32000000
number=32000000
s=0
for i in range(number):
    s=s+i

starttime2 = datetime.datetime.now()

proctime=starttime2-starttime1

print('calculate the sigma_i=%s'% number,'the time took is %s'% proctime)

