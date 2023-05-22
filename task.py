#function to calculate discount 
def calcu_dis_price(qt, price, dis_percentage):
    if qt > 15:
        dis_qt = qt - 15
        return (15 * price) + (dis_qt * price * (1 - dis_percentage))
    else:
        return qt * price

#function to define discount rules
def dis_rules(qt, cart_tot):
    dis_amt = 0
    dis_name = ""

    if cart_tot > 200:
        dis_amt = 10
        dis_name = "flat_10_discount"
    elif any(qty > 10 for qty in qt):
        dis_amt = sum(price * qty * 0.05 for price, qty in zip(prices, qt))
        dis_name = "bulk_5_discount"
    elif sum(qt) > 20:
        dis_amt = cart_tot * 0.1
        dis_name = "bulk_10_discount"
    elif sum(qt) > 30 and any(qty > 15 for qty in qt):
        excess_qt = sum(qty - 15 for qty in qt if qty > 15)
        dis_amt = excess_qt * price * 0.5
        dis_name = "tiered_50_discount"

    return dis_name, dis_amt

#function to find the tot cost after considering discount
def calcu_tot_cost(qt, wrapped_gifts):
    prdt_tot = []
    cart_tot = 0

    for i in range(len(prdts)):
        prdt_name = prdts[i]
        price = prices[i]
        qty = qt[i]
        wrapped = wrapped_gifts[i]

        prdt_amt = qty * price
        prdt_tot.append((prdt_name, qty, prdt_amt))
        cart_tot += prdt_amt

        if wrapped:
            cart_tot += qty * gift_wrap_fee

    dis_name, dis_amt = dis_rules(qt, cart_tot)

    shipping_fee = (sum(qt) // 10) * shipping_fee_per_package
    total_cost = cart_tot - dis_amt + shipping_fee

    return prdt_tot, cart_tot, dis_name, dis_amt, shipping_fee, total_cost

#catalog
prdts = ["Product A", "Product B", "Product C"]
prices = [20, 40, 50]

#fees
gift_wrap_fee = 1
shipping_fee_per_package = 5 #(10 in one pkg)

#list initialization of quantities and wrapped gift or not
qt = []
wrapped_gifts = []

#input value quantity of each product and if it's a wrapped gift
for prdt in prdts:
    qty = int(input(f"Enter the qt of {prdt}: "))
    wrapped = input(f"Is {prdt} wrapped as a gift? (yes/no): ").lower() == "yes"
    qt.append(qty)
    wrapped_gifts.append(wrapped)
    
#calculating tot cost
prdt_tot, subtot, dis_name, dis_amt, shipping_fee, tot = calcu_tot_cost(qt, wrapped_gifts)

#output display
print("\nProduct Details:")
for prdt in prdt_tot:
    print(f"{prdt[0]} - Quantity= {prdt[1]}, Total Amount= ${prdt[2]}")

print(f"\nSubtotal= ${subtot}")
print(f"Discount Applied= {dis_name}, Amount= ${dis_amt}")
print(f"Shipping Fee= ${shipping_fee}, Gift wrap fee= ${gift_wrap_fee}")
print(f"Total= ${tot}")
