arr = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
target = 8

# Import the bisect module
import bisect 

# Call the module and provide the array and the target value
index = bisect.bisect_left(arr, target) 

#Print results
if index < len(arr) and arr[index] == target:
    print(f"Bisect: Target found at index {index}")
else:
    print("Bisect: Target not found")