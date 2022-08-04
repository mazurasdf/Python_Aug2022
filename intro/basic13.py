# Print all the integers from 1 to 255.
# for i in range(1,256):
#     print(i)

# Print integers from 0 to 255, and with each integer print the sum so far.
# sum = 0
# for i in range(0,256):
#     sum = i + sum
#     print(sum)
# print("final sum is below")
# print(sum)

# Given an array, find and print its largest element.
# arr = [1,0,-18,14,2,100,6,2,5,0,99,101,18]
# arr = [-4,-18,-3,-100,-42]
# max = arr[0]
# for num in arr:
#     if max < num:
#         max = num
# print(max)

# Analyze an array’s values and print the average
arr = [1,0,-18,14,2,100,6,2,5,0,99,101,18]
sum = 0
for num in arr:
    sum = sum + num
# print(sum)
avg = sum/len(arr)
print(avg)