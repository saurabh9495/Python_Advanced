# Basic Method

# n = int(input())
# arr = [int(x) for x in input().split()]
# summation = 0
# for x in arr:
#     summation += x
# print(summation)

# Faster Method

# import builtin standard input and output
# from sys import stdin, stdout

# def main():
#     n = stdin.readline()
#     arr = [int(x) for x in stdin.readline().split()]

#     summation = 0
#     for x in arr:
#         summation += x

#     stdout.write(str(summation))
#     stdout.write("\n")

#     summation = sum(arr)
#     stdout.write(str(summation))


# if __name__ == "__main__":
#     main()

# Fastest Method


# import libraries for input/ output handling 
# on generic level 
import atexit, io, sys 
  
# A stream implementation using an in-memory bytes  
# buffer. It inherits BufferedIOBase. 
buffer = io.BytesIO() 
sys.stdout = buffer
  
# print via here 
@atexit.register 
def write(): 
    sys.__stdout__.write(buffer.getvalue()) 
   
n = int(input()) 
  
# input the array 
arr = [int(x) for x in input().split()] 
  
# initialize variable 
summation = 0
  
# calculate sum 
for x in arr: 
    summation += x 
  
# print answer 
print(summation) 