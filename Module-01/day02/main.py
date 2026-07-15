# Class Exercise
total = float(input("Enter the total amount in ETB: "))
people = int(input("Enter the number of people: "))

def split_bill(total,people,tip_rate=0.10):
    amount = (total*(1+tip_rate))/people
    return amount

names = str(input("Enters the names of your friends separated by space: "))

friends = names.split()



for name in friends:
    print(f"{name}'s share is {split_bill(total,people)}")
