gadget = int(input('Enter total number of gadget: '))
mrp = int(input('Price: '))

if gadget < 14:
    print('No discount for this much gadgets.')
    print('Pay Rs. ', mrp)

elif(gadget>14 and gadget<20):
    tot_price2 = mrp * gadget
    dis1 = 10 / 100 * tot_price2
    print("The total price is ", tot_price2)
    print("After 10 percentage discount")
    print("The discounted price is: ", tot_price2 - dis1)
elif gadget >= 20:
    discountPrice = mrp * 15/100
    total = discountPrice
    print(f'MRP: Rs.{mrp}\nDiscount: {discountPrice}\nTotal Price: {total}')

