# %% uniqe cities
cities = ["Diredawa","Addis Ababa","Gondar","Bahirdar","Gondar","Addis Ababa"]

unique_cities = set(cities)
print(unique_cities)

# %% price report
groceries = {"bread": 100, "Banana":120, "Orange":250,"Holland":110, "Abuwoled":50}
for key,value in groceries.items():
    print(key, value)
# %% Tax Comprehension and cheap items 
prices = [100,250,400,80]
taxed_values = [val * 0.15 for val in prices ]
print(f"here are the price with 15% tax:{taxed_values}")
cheap_prices =[val for val in prices if val < 200]
print(f"here are cheap prices:{cheap_prices}")

# %% Write and Read 

name_list = ["Abebe", "Tsega", "Desta"]

with open("names.txt", "w") as file:
   for name in name_list:
       file.write(name + "\n")


with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())



# %% Safe Division

while True:
 n = (input("Enter a divisor:"))
 try:
  quotient = 1000/int(n)
  print(quotient)
 except ValueError:
    print("invalid input!")
 except ZeroDivisionError:
    print("Can not divide by Zero!")
 
 confirm = (input("do you want to continue (Y/N)"))
 if confirm.upper() != "Y":
     break


# %%
