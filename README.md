# Banana Pi Benchmark
 it is for Banan Pi and Raspberry Pi3 and Pi4 benchmark \

 Banana Pi BPI M64 , under raspian OS
 Raspberry Pi3 and Pi4 , run same raspian OS

 run the python on the spyder tools on Windows

 The code is in bannapi_benchmark.py, it is very short code 

 Get the following result of benchmark
 Jan-27-2020: add the number product benchmark


# it is based on Banana Pi 4 of Ben Chen
# i=1000000, the run time is  0:00:01.477372 
# i=2000000, the run time is  0:00:02.821595 
# i=4000000, the run time is  0:00:05.771449 
# i=8000000, the run time is  0:00:11.046958 
# it is based on Raspberry Pi 3 
# 
# i=1000000, the run time is  0:00:05.516682 
# i=2000000, the run time is  0:00:13.147322 
# i=4000000, the run time is  0:00:23.348977 
# i=8000000, the run time is  0:00:48.460275 
  
# it is based on Lenovo T480 Notebook, Intel i5 
# 
# i=1000000, the run time is  0:00:00.217468 
# i=2000000, the run time is  0:00:00.394966 
# i=4000000, the run time is  0:00:00.872085 
# i=8000000, the run time is  0:00:01.323677 
# i=32000000, the run time is  0:00:05.210840 
======================================Wisdom data is as follows===================

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

Jan-27-2020: add the number product benchmark

From bananapi BPI M64

>>> %Run bananapi_benchmark2.py
The number product result is 456569 digits long.
Took 18.57682967185974 seconds to calculate.
calculate the sigma_i=32000000 the time took is 0:00:10.023055

from Wisdom Lenovo E480

runfile('D:/Tools/Python_tools/Python_examples/BPI_M64/bananapi_benchmark.py', wdir='D:/Tools/Python_tools/Python_examples/BPI_M64')
The number product result is 456569 digits long.
Took 2.5871317386627197 seconds to calculate.
calculate the sigma_i=32000000 the time took is 0:00:03.049287

# download it from github to ubuntu