
temp_burger_price = 2000

for i in range(3):
    price = int(input())
    if(temp_burger_price > price):
        temp_burger_price = price

temp_juice_price = 2000

for j in range(2):
    price = int(input())
    if(temp_juice_price > price):
        temp_juice_price = price

print(temp_burger_price + temp_juice_price - 50)
