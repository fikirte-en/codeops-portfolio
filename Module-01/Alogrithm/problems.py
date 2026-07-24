# %%  arrays that print even numbers with even indexes
def getOnlyEvens(arr):
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] %  2 == 0:
            print(arr[i])
        else:
            return None    
getOnlyEvens([1, 2, 3, 6, 4, 8]) 
# %% reverse compare
def reverseCompare(num):
    if not 10<= num <= 99:
        raise ValueError("the number must be two digit!")
    reversed_num = int(str(num)[::-1])
    if reversed_num <= num:
        print ("ok!")
    else:
        print("not ok!")
    return reversed_num
reverseCompare(72)
reverseCompare(23)
reverseCompare(11)
# %%  factorial of a number 
def returnFactorial(num):
    while num >= 0:
        if num == 1 or num == 0:
            return 1
        return num * returnFactorial(num-1)
print(returnFactorial(5))
print(returnFactorial(6))
print(returnFactorial(0))
        

# %% Merra Array
def checkMeera(arr):
    if not all(isinstance(x, (int, float)) for x in arr):
        return "Invalid array: contains non-numeric values."
    for x in arr:
        if x * 2 == x:   
            return "I am not a Meera array."
    return "I am a Meera array."
checkMeera([10, 4, 0, 5])
checkMeera([7, 4, 9])
checkMeera([1, -6, 4, -3])
# %% Dual array
def isDual(arr):
    for i in range(len(arr)):
        if 
