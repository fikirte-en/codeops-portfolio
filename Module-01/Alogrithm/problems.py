# %%  arrays that print even numbers with even indexes
def getOnlyEvens(arr):
    result = []
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] %  2 == 0:
            result.append(arr[i])
    print (result)   
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
    return None
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
        print("Invalid array: contains non-numeric values.")
        return

    for n in arr:
        if n * 2 in arr:
            print("I am NOT a Meera array")
            return

    print("I am a Meera array")


checkMeera([10, 4, 0, 5])   
checkMeera([7, 4, 9])       
checkMeera([1, -6, 4, -3])  


# %% Dual array
def isDual(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1

    for value in counts.values():
        if value != 2:
            return 0

    return 1
nums = {1, 2, 1, 3, 3, 2}
isDual(nums)

# %% digital clock
def digitalClock(seconds):
    seconds = seconds % 86400   

    hours = seconds // 3600
    remaining = seconds % 3600
    minutes = remaining // 60
    secs = remaining % 60

    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


print(digitalClock(5025))    
print(digitalClock(61201))  
print(digitalClock(87000))  
# %%
