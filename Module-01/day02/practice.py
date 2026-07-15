# %%
user_input = 'Y'   

while user_input == 'Y':
    temp = int(input("Enter the temperature in celsius: "))
    if temp < 15:
        print("cold")
    elif 15 <= temp <= 28:
        print("warm")
    else:
        print("hot")

    user_input = input("Do you want to continue (Y/N): ").upper()
    if user_input == 'Y':
        continue
    elif user_input== 'N':
        break
    else:
        print("invalid input!")

# %% Reciept Loop
for i in range(1,11):
    print(f"Receipt #{i}")
    

# %% Even numbers 
for i in range(1,21):
    if i % 2 == 0:
        print (i)
    else:
        continue

# %% discount function
def apply_discount(price,percent=10):
    price = price * percent
    return price 
apply_discount(100,20)

# %% Countdown
i = 5
while i >= 0:
    print(i)
    i-=1
print("Litoff!")

# %%
