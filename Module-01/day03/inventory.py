# Building a path relative to the script itself
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"stock.txt")
stock= {}
try:
 with open(file_path, "r") as f:
     
     for line in f:
        line = line.strip()
        if not line:
           continue
        item,qty = line.strip().split(",")
        stock[item] = int(qty)
except FileNotFoundError:
   print("No stock file found!")

def update(item,amount):
   stock[item] = stock.get(item,0) + amount


def write_update(file_path,stock):
   with open(file_path, "w") as f:
        for item, qty in stock.items():
            f.write(f"{item},{qty}\n")


# gather input
while True:
    item = input("Which item? ")
    amount = int(input("How much? (use negative to subtract): "))
    update(item, amount)
    write_update(file_path, stock)   # inside the loop — save every time

    low = [item for item, qty in stock.items() if qty < 10]
    print("low stock:", low)

    again = input("Type 'done' to finish, or 'continue' to keep going: ")
    if again == "done":
        break
