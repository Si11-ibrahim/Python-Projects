basePrice = int(input("price: "))

gst = basePrice * 20/100

tax = (basePrice * 17/100) +gst

totalPrice = basePrice + gst + tax

print(f"GST: Rs.{gst}")
print(f'Tax: Rs.{tax}')
print(f'Total price: Rs.{totalPrice}')
