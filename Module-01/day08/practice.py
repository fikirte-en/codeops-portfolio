# %% recirsive sum


def totals(nums):
   if not nums:
      return 0
   first = nums[0]
   rest = nums[1:]
   return first + totals(rest)
nums = [1,2,3]
total = totals(nums)
print(total)
      

# %% Binary Search


def binary_search(items,low,high,target):
   if high>=low:
      mid = (low + (high-low))//2

      if items[mid]==target:
       return mid
      elif items[mid] <= target:
       return binary_search(items, mid+1,high, target)  
      else:
       return binary_search(items,low,mid-1,target)   
   else:
      return -1
items=[12,45,67,13,8]
s = binary_search(items,0,len(items),67)
if s != -1:
   print("the target is found at: ",s)
else:
   print("the target is not present! ")
      
   


# %% Merge Sort 
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])   
    result.extend(right[j:])
    return result

def merge_sort(items):
    if len(items) <= 1:              
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])   
    right = merge_sort(items[mid:])  
    return merge(left, right)        

print(merge_sort([5, 2, 8, 1]))  

# %% sort with a key 
accounts = [("Amanuel", 4200), ("Selam", 1800), ("Biruk", 9500), ("Hana", 3000)]

sorted_accounts = sorted(accounts, key=lambda a: a[1], reverse=True)
print(sorted_accounts)

# %% two pointers 
def has_pair(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return True
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return False

balances = [100, 250, 400, 800, 1500]
print(has_pair(balances, 1150))  
# %%
